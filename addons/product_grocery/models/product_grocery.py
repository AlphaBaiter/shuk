# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_grocery(models.Model):
    _name = 'product_grocery.product_grocery'
    _description = 'product_grocery.product_grocery'

    no_inventory_managment = fields.Boolean(
        'In active', default=False)