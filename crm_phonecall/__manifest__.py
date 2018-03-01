# -*- coding: utf-8 -*-

{
    "name": "CRM Phone Calls",
    "version": "11.0.1.1.1",
    "category": "Customer Relationship Management",
    "author": "Odoo Agency<vishal@odoo.agency>",
    "website": "http://odoo.agency",
    "depends": [
        'crm',
        'calendar',
        'sale',
        'sales_team',
        'sale_management',
    ],
    "data": [
        'security/crm_security.xml',
        'security/ir.model.access.csv',
        'wizard/crm_phonecall_to_phonecall_view.xml',
        'views/crm_phonecall_view.xml',
        'views/res_partner_view.xml',
        'views/crm_lead_view.xml',
        'report/crm_phonecall_report_view.xml',
    ],
    'installable': True,
}
