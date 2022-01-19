# Copyright 2019 EINFO HSP
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': "Relative field forbid quick create by HSP",

    'summary': "屏蔽many2one many2many 等直接创建按钮",
   'license': 'LGPL-3',
   'description': """
    屏蔽many2one many2many 等直接创建按钮
   """,
    'author': 'HSP',
    'website': "https://www.garage-kit.com",
    'images': ['static/description/logo.png'],
    'category': 'Tools',
    'version': '13.0.1.0.0',
  
    'depends': [
        'base', 'web',
    ],
    'data': [
        'views/view.xml'
    ],
    # 'demo': [
    #     'demo/report.xml',
    # ],
    'installable': True,
}
