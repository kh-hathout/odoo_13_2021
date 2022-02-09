# -*- coding: utf-8 -*-
{
    'name': "Electronic invoice - Saudi | Sales & Purchase | QR Code",
    'description': """
      E-invoice - Saudi - Sales & Purchase
       Electronic invoice KSA
       Customer Invoice QRCode Builder
       Dynamic QR Code Builder For Customer Invoice, For Electronic Invoice Requirements
    """,
    'author': "F-Team",
    'email': "prog.ahmed.eid@gmail.com",
    'category': 'accounting',
    'version': '0.1',
    'price': 20,  
    'currency': 'EUR',
    'license': 'AGPL-3',
    'images': ['static/description/main_screenshot.png'],
    'depends': ['base', 'account', 'sale', 'purchase'],
    'data': [
        'views/partner.xml',
        'reports/invoice_inherit_report.xml',
    ],
}
