# -*- coding: utf-8 -*-
from odoo import http


class ProductsController(http.Controller):

    @http.route(['/get_products'], type='json', auth='public', website=True)
    def get_products(self, **kw):
        """ Get Products using AJAX request """

        ## The first 10 products published
        products = http.request.env['product.template'].sudo().search([('website_published', '=', True)], limit=10)

        product_item = []
        for product in products:
            item = {
                "name":product.name,
                "id":product.id,
            }
            product_item.append(item)

        return product_item

