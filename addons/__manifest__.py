# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Demo Odoo',
    'version': '1.1',
    'category': 'Demo Odoo',
    'sequence': 10,
    'summary': '',
    'depends': [
        'sale',
        'fleet',
    ],
    'description': "It is a module for writing basic odoo.",
    'data': [
        'views/basic_views_menus.xml',
        'views/basic_action.xml',
        'views/basic_views.xml',
        'views/fleet_views_menus.xml',
    ],
    'qweb': [],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
