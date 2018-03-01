# -*- coding: utf-8 -*-

{
    "name": "CRM Phone Calls Task",
    "version": "11.0.1.1.1",
    "category": "CRM Phone Calls Task",
    "author": "Odoo Agency <vishal@odoo.agency>",
    "website": "https://odoo.agency",
    "depends": [
        'crm_phonecall', 'project'
    ],
    "data": [
        'views/crm_phonecall_view.xml',
        'views/res_config_view.xml',
    ],
    'installable': True,
}
