# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    phonecall_ids = fields.One2many(
        comodel_name='crm.phonecall',
        inverse_name='partner_id',
        string='Phonecalls',
    )
    phonecall_count = fields.Integer(
        compute='_compute_phonecall_count',
        string="Phonecalls",
    )

    @api.multi
    def _compute_phonecall_count(self):
        for partner in self:
            partner.phonecall_count = self.env[
                'crm.phonecall'].search_count(
                [('partner_id', '=', partner.id)])
