# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Student Result Portal',
    'version': '1.0',
    'author': 'Sakib',
    'sequence': 1,
    'category': 'Inventory/Purchase',
    'summary': '',
    'description': "",
    'depends': [],
    'demo': [

        ],
    'data': [
        'views/menus.xml',
        'views/exam.xml',
        'views/student.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
