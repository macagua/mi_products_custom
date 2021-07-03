# -*- coding: utf-8 -*-
{
    'name': "Moldeo Interactive Custom",
    'summary': "Moldeo Interactive Products Customizations",
    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and use
        JavaScript functionalities in Odoo 13.

        Source: https://www.youtube.com/c/moldeointeractive/search?query=odoo%20javascript
    """,
    'version': '13.0.1',
    'author': 'Moldeo Interactive',
    'website': 'https://www.moldeointeractive.com.ar/',
    'support': 'info@moldeointeractive.com.ar',
    'maintainer': 'Leonardo J. Caballero G. <leonardocaballero@gmail.com>',
    'license': 'AGPL-3',
    'category': 'Tutorial',
    'depends': [
        'base',
        'product',
        'web',
        'website',
        'website_sale'
    ],
    'data': [
        'views/web_asset_backend_template.xml',
    ],
    'qweb': [],
    'demo': [],
    'images': [
        'static/description/icon.png'
    ],
    'installable': True,
    'application': True,
}

