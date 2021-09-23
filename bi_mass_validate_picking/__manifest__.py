# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Mass Validate Picking (Delivery/Receipt)",
    "version" : "13.0.0.0",
    "category" : "Warehouse",
    'summary': 'Mass validate picking mass confirm picking mass validate delivery mass confirm delivery mass validate receipt mass confirm receipt validate mass picking confirm mass picking validate multiple delivery validate multiple picking in single click mass receipt',
    "description": """

                    Mass Validate Picking (Delivery/Receipt) in odoo,
                    Mass validate picking under sale order in odoo,
                    Mass validate picking under purchase order,
                    Multiple picking order validate by single click in odoo,
                    Mass picking order done in odoo,
                    Validate multiple picking under confirmed sale order in odoo,
                    Validate multiple picking under confirmed purchase order in odoo,
                    Raise warning/validate if order is not in confirmed state in odoo,

                """,
    "author": "BrowseInfo",
    "website" : "https://www.browseinfo.in",
    "price": 30,
    "currency": 'EUR',
    "depends" : ['base','purchase','stock', 'sale', 'sale_management'],
    "data": [
            'wizard/mass_validate_picking.xml',
            ],
    'qweb': [],
    "auto_install": False,
    "installable": True,
    "live_test_url":'https://youtu.be/yZ4zHujMEhw',
    "images":["static/description/Banner.png"],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
