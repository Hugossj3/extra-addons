# -*- coding: utf-8 -*-
{
    'name': "Modulo-hugo",

    'summary': """
        Modulo creadito con el Scaffolding, sincronizado con github""",

    'description': """
        Este Modulo esta para experimentar como ratas de laboratorio
    """,

    'author': "Hugo(The Goat)",
    'website': "https://github.com/Hugossj3/extra-addons",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application":True,
    "installable":True
}
