# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductGroceryTemplate(models.Model):
    _name = 'product.template_grocery'
    _description = 'Product'
    _inherit = ['product.template']