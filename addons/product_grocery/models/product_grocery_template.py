#-*- coding: utf-8 -*-

from odoo import models, fields, api


class product_grocery(models.Model):
    _inherit = 'product.template'
    
    _name = 'product_grocery.product'
    _description = 'Information about product_grocery'

    name = fields.Char()
    no_inventory_management = fields.Boolean(string='No Inventory Management')
    
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

