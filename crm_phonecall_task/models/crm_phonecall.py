# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from functools import reduce
from odoo.tools.safe_eval import safe_eval


class CrmPhonecall(models.Model):
    """ Model for CRM phonecalls """
    _inherit = "crm.phonecall"

    @api.multi
    def convert_task(self):
        partner = self.env['res.partner']
        task = self.env['project.task']
        task_dict = {}
        for call in self:
            task_id = task.search([('call_id', '=', call.id)])
            if not task_id:
                partner_id = call.partner_id and call.partner_id.id or False
                user_id = call.user_id and call.user_id.id or False
                project_id = safe_eval(
                    self.env['ir.config_parameter'].get_param(
                        'crm_phonecall_issue.project_id', 'False'
                    )
                )
                task_id = task.create({
                    'name': call.name,
                    'partner_id': partner_id or False,
                    'email_from': call.partner_id and call.partner_id.email or '',
                    'user_id': user_id,
                    'call_id': call.id,
                    'project_id': project_id and int(project_id) or False,
                    'description': call.description or ''
                })
            task_dict[call.id] = task_id
        return task_dict

    @api.multi
    def action_button_convert2task(self):
        task_dict = {}
        task_dict = self.convert_task()
        if task_dict:
            key, value = task_dict.popitem()
            return value.redirect_task_view()
        return False



class projectTask(models.Model):
    _inherit = 'project.task'

    call_id = fields.Many2one('crm.phonecall', "Phone Calls")

    @api.multi
    def redirect_task_view(self):
        self.ensure_one()
        # Get opportunity views
        form_view = self.env.ref('project.view_task_form2')
        tree_view = self.env.ref('project.view_task_tree2')
        return {
            'name': _('Task'),
            'view_type': 'form',
            'view_mode': 'tree, form',
            'res_model': 'project.task',
            'res_id': self.id,
            'view_id': False,
            'views': [
                (form_view.id, 'form'),
                (tree_view.id, 'tree'),
            ],
            'type': 'ir.actions.act_window',
        }
