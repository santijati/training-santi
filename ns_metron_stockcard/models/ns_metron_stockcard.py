# -*- coding: utf-8 -*-
from odoo import api, models, fields


class NsStockCard(models.Model):
    _name = 'ns.stock.card'
    # ns_catid = fields.Many2one('product.category', 'Category',
    #                            domain='[("display_name","=","All / Consumable"),("display_name","=","All / Stockable")]')
    # ns_prod = fields.Many2one(
    #     'product.product', 'Product Name', domain='[("categ_id","in",ns_catid)]')
    ns_prod = fields.Many2one(
        'product.template', 'Product')
    ns_loc = fields.Selection(selection=[(
        'all', 'All Location'), ('select', 'Select Location')], string="Location", default="select")
    ns_start = fields.Date('Start Date')
    ns_end = fields.Date('End Date')
    with_internal_transfer = fields.Boolean('')
    ns_stockloc = fields.Many2one(
        'stock.location', string="Stock Location")
