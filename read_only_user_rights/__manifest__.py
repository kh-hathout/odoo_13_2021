# For any query or any odoo related work,
# Email us: shivoham.odoo@gmail.com
{
    'name': 'Make User Readonly For Specific Model | Limited Access Rights to Login User | Readonly Access Rights to User | Maker User Readonly',
    "author": "Shivoham",
    'version': '13.0',
    'price': '25.0',
    'currency': 'USD',
    'summary': "Make User Readonly for particular model or Whole Project",
    'description':
        """Make User Readonly for specific models or make whole project readonly for particular user.""",
    "license": "LGPL-3",
    'depends': ['base', 'sale_management'],
    'data': [
        'security/user_read_only_group.xml',
        'security/ir.model.access.csv',
        'views/res_user_read_only.xml',
    ],
    'images': [
        'static/description/banner.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
