# -*- coding: utf-8 -*-
{
    'name': "Videoclub_sge",

    'summary': """
        Esto es un intento de tener un modulo propio""",

    'description': """
        A veces hago cambios aqui cuando el github no me detecta los campos, patatas al carbon
    """,

    'author': "My Company",
    'website': "https://github.com/Hugossj3/extra-addons",
    'license':"AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/videoclub_security.xml',
        'security/ir.model.access.csv',
        'views/videoclub.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable':True,
}
