# -*- coding: utf-8 -*-
# from odoo import http


# class ProductGrocery(http.Controller):
#     @http.route('/product_grocery/product_grocery', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_grocery/product_grocery/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_grocery.listing', {
#             'root': '/product_grocery/product_grocery',
#             'objects': http.request.env['product_grocery.product_grocery'].search([]),
#         })

#     @http.route('/product_grocery/product_grocery/objects/<model("product_grocery.product_grocery"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_grocery.object', {
#             'object': obj
#         })

