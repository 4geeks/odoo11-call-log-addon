# -*- coding: utf-8 -*-

from odoo import fields, models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    phonecall_id = fields.Many2one(
        comodel_name='crm.phonecall',
        string='Phonecall',
    )
