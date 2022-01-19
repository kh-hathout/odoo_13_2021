# -*- coding: utf-8 -*-
{
    'name': 'Number of row in One2many tree view',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Show number of row in One2many tree view',
    'author': 'Init Co. Ltd',
    'support': 'contact@init.vn',
    'website': 'https://init.vn/?utm_source=odoo-store&utm_medium=13&utm_campaign=one2many-row-number',
    'license': 'LGPL-3',
    'description': """""",
    'depends': [
        'web',
    ],
    'data': [
        # data

        # view
        "views/one2many_row_number.xml",

        # wizard

        # report

        # menu

        # security
    ],
    'qweb': [
        # 'static/src/xml/*.xml',
    ],
    'demo': [],
    'test': [],
    'images': ['static/description/banner.png'],
    'bootstrap': True,
    'installable': True,
}
