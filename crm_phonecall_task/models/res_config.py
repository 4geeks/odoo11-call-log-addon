# -*- coding: utf-8 -*-
from odoo import models, fields, SUPERUSER_ID, api
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    project_id = fields.Many2one('project.project',
        string="Project"
    )

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrConfigParam = self.env['ir.config_parameter'].sudo()
        res.update(
            project_id=literal_eval(IrConfigParam.get_param('crm_phonecall_issue.project_id', default='False')),
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        IrConfigParam = self.env['ir.config_parameter'].sudo()
        IrConfigParam.set_param('crm_phonecall_issue.project_id', repr(self.project_id and self.project_id.id or False))
