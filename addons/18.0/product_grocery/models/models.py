# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class product_grocery(models.Model):
#     _name = 'product_grocery.product_grocery'
#     _description = 'product_grocery.product_grocery'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

