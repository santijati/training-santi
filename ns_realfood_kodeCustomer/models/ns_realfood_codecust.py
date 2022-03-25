# -*- coding: utf-8 -*-
from odoo import api, models, fields


class NsCodeCustomer(models.Model):
    _name = 'ns.code.customer'
    _rec_name = 'ns_name'
    ns_name = fields.Char('Customer Type Name', required=True)
    ns_mode = fields.Selection(selection=[(
        'single', 'Single'), ('manual', 'Manual')], string="Customer Type Mode", required=True)
    ns_code = fields.Char('Customer Code')


class NsCustomer(models.Model):
    _inherit = 'res.partner'
    ns_type = fields.Many2one(
        'ns.code.customer', string='Customer Type', ondelete='restrict')
    ns_cust_id = fields.One2many(
        'res.partner', 'ns_type', string="Customer Code")
    ns_code_type = fields.Char(string='Customer Code')
    ns_code = fields.Char(string='Customer Code', default='')

    @api.onchange('ns_type')
    def _codetype(self):
        # nama mode nya
        q = self.env['ns.code.customer'].browse(self.ns_type.id)
        self.ns_code_type = q.ns_mode
        qmode = q.ns_mode
        qcode = q.ns_code
        if qmode == 'single':
            self.ns_code = qcode