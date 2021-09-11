# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api


class account_move(models.Model):
    _inherit = "account.move"

    def sh_mass_invoice_confirm(self):
        
        account_invoice_obj = self.env['account.move']
        active_ids = self.env.context.get('active_ids')
        if active_ids:
            for active_id in active_ids:
                search_invoice_rec = account_invoice_obj.search([('id', '=', active_ids)], limit=1)
                if search_invoice_rec:
                    search_invoice_rec.action_post()

