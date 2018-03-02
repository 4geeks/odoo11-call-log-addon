# -*- coding: utf-8 -*-
{
    'name': 'CRM Service Activty',
    'version': '11.0.1.0.0',
    'author': 'Odoo Agency. <vishal@odoo.agency>',
    'website': 'http://odoo.agency',
    'category': 'base',
    'summary': 'Main Service Activity',
    'depends': [
        'contacts','crm_phonecall_task','res_partner_active_type'
    ],
    'data': [
        'views/menu.xml',
    ],
    'qweb': [
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
