# -*- coding: utf-8 -*-
{
    'name': "Books ISBN",

    'summary': """
        Get Books Data based on ISBN""",

    'description': """
         Get Books Data based on ISBN
    """,

    'author': "Federico Medici",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['iap', 'my_library'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/library_books_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    "installable":True,
    "application":True
}
