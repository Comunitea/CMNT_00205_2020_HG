# -*- coding: utf-8 -*-
{
    'name': 'Handy Gym Theme',
    'version': '10.0.0.0.0',
    'summary': 'Handy Gym Customization Theme',
    'author': 'Comunitea',
    'license': 'AGPL-3',
    'category': 'Website',
    'depends': [
        'web',
        'website',
        'website_crm',
        'website_legal_page',
        'website_sale',
        'website_sale_wishlist',
        'website_signup_legal_page_required',
    ],
    'data': [
        'data/website_data.xml',
        'data/menu_data.xml',
        'data/page_data.xml',
        'templates/assets.xml',
        'templates/checkout.xml',
        'templates/contact.xml',
        'templates/footer.xml',
        'templates/header.xml',
        'templates/legal.xml',
        'templates/login.xml',
        'templates/product.xml',
        'templates/shop.xml',
        'views/product_view.xml',
        'views/res_config.xml',
    ],
    'images': [
        'static/description/icon.png'
    ],
    'website': 'http://www.comunitea.com',
    'installable': True,
}
