# -*- coding: utf-8 -*-
{
    'name' : "MRP Secondary Unit of Measure-UOM",
    "author": "Edge Technologies",
    'version': '13.0.1.0',
    'sequence':'1',
    'live_test_url': "https://youtu.be/xjlbK_ttdpw",
    "images":['static/description/main_screenshot.png'],
    'summary': 'Manufacturing secondary unit of measure for Manufacturing order secondary unit of measure for MRP secondary unit of measure mrp secondary uom Manufacturing secondary uom for Manufacturing secondary uom for mrp secondary uom for production secondary uom',
    'description' : '''
        secondary unit of measure For Manufacturing app In Odoo.
    ''',
    
    "license" : "OPL-1",
    'depends' : ['mrp','sale_management'],
    'data': [
            'security/secondary_uom_group.xml',
            'security/ir.model.access.csv',
            'views/mrp_sec_uom.xml',
            'views/mrp_production_report.xml',
            'views/product_view.xml',
            'views/stock_quant_view.xml',
             ],
    'installable': True,
    'auto_install': False,
    'price': 25,
    'currency': "EUR",
    'category': 'Manufacturing',
}    