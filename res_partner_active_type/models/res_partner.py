from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    active_type = fields.Selection([
        ('active', 'ACTIVE'),
        ('inactive', 'INACTIVE'),
        ('donotgo', 'DO NOT GO'),
        ('cod', 'COD'),
    ], string='Active Type')