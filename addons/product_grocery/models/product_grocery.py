# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductGrocery(models.Model):
    _name = 'product.product_grocery'
    _description = 'Product'

    no_inventory_managment = fields.Boolean(
        'is inventory managment', default=False)
    bottle_deposit = fields.Boolean(
        'is bottle deposit', default=False)
