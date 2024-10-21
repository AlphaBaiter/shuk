# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductGrocery(models.Model):
    _name = 'product.product_grocery'
    _description = 'Product'

    # חסימות
    max_sales = fields.Float(
        'Max sale')
    min_sales = fields.Float(
        'Min sale')
    block_sales = fields.Datetime()
    block_purchase = fields.Datetime()
    block_pos = fields.Datetime()

    #פיקדון בקבוקים
    is_deposit_bottle = fields.Boolean(
        'Is bottle deposit', default=False)
    deposit_attached = fields.Integer(
        "Count attached deposit", default=0)
    #deposit_type = fields.One2many(
    #   'product.packaging', 'product_id', 'Product Packages',

    #כשרויות
    leaven = fields.Boolean(
        'Is leaven', default=False)
    kosher_passover = fields.Boolean(
        'Is passover kosher', default=False)

    #משקל
    content = fields.Float(
        'Product content')
    tara = fields.Float(
        'Product tara')

    #כללי
    is_returnable = fields.Boolean(
        'Is returnable', default=True)
    is_age_limited = fields.Boolean(
        'Is age limited', default=False)
    #manufacturing_country= fields.One2many(
    #   'product.packaging', 'product_id', 'Product Packages',

    #POS
    is_returnable_pos = fields.Boolean(
        'Is returnable at POS', default=True)

    # ממשק חיצוני
    is_price_transparency = fields.Boolean(
        'Is price transparency displayed', default=False)