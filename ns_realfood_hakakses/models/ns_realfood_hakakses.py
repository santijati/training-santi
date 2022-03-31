# -*- coding: utf-8 -*-
from odoo import api, models, fields, exceptions


class NsOrder(models.Model):
    _inherit = 'sale.order'
    paid = fields.Boolean('')

    def action_confirm(self):
        self.paid = True

        if not self.env.user.has_group('ns_realfood_hakakses.confirmso'):
            raise exceptions.UserError('You dont have access to confirm SO')

        return super(NsOrder, self).action_confirm()

    def action_cancel(self):
        self.paid = False

        if not self.env.user.has_group('ns_realfood_hakakses.cancelso'):
            if self.state == 'sale' or self.state == 'done' or self.state == 'cancel':
                raise exceptions.UserError('You dont have access to cancel SO')

        return super(NsOrder, self).action_cancel()
