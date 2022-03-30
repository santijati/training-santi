# -*- coding: utf-8 -*-
from odoo import api, models, fields


class NsStockCard(models.Model):
    _name = 'ns.stock.card'
    ns_prodid = fields.Integer('Product Id')
    ns_prod = fields.Many2one(
        'product.product', 'Product')
    ns_loc = fields.Selection(selection=[(
        'all', 'All Location'), ('select', 'Select Location')], string="Location", default="select")
    ns_start = fields.Date('Start Date')
    ns_end = fields.Date('End Date')
    with_internal_transfer = fields.Boolean('')
    ns_stockloc = fields.Many2one(
        'stock.location', string="Stock Location")
    ns_movestock = fields.One2many('stock.move.line', 'id', 'Product Move')


class StockReport(models.AbstractModel):
    _name = 'report.ns_metron_stockcard.stockcard_report_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name(
            'ns_metron_stockcard.stockcard_report_template')
        obj = self.env['ns.stock.card'].browse(docids)
        obj_stock = self.env['stock.move.line'].search(
            [('date', '>=', obj.ns_start), ('date', '<=', obj.ns_end), ('product_id', '=', obj.ns_prod.id)])

        stock = []
        if obj.ns_loc == 'select':
            for rec in obj_stock:
                if obj_stock.location_id == obj.ns_stockloc.id or obj_stock.location_dest_id == obj.ns_stockloc.id:
                    stock.append({'reference': rec.reference, 'date': rec.date, 'from': rec.location_id.name, 'to': rec.location_dest_id.name,
                                  'partner': rec.company_id.name, 'in': rec.product_uom_qty, 'out': rec.qty_done, 'balance': rec.product_qty})
        else:
            for rec in obj_stock:
                stock.append({'reference': rec.reference, 'date': rec.date, 'from': rec.location_id.name, 'to': rec.location_dest_id.name,
                              'partner': rec.company_id.name, 'in': rec.product_uom_qty, 'out': rec.qty_done, 'balance': rec.product_qty})
        data = {
            'stock': stock
        }
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self.env[report.model].browse(docids),
            'data': [data],
        }
        return docargs
