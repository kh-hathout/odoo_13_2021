# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import fields, models, api


class MRPProduction(models.Model):

    _inherit = 'mrp.production'

    sale_id = fields.Many2one('sale.order', string='Sale Order')
    sale_line_id = fields.Many2one(
        'sale.order.line', string='Sale Order Line',
        compute="_compute_sale_line_id", store=True)

    # To compute sale order line if production created from sale order
    @api.depends('sale_id')
    def _compute_sale_line_id(self):
        for order in self:
            order.sale_line_id = False
            if order.sale_id:
                line = order.sale_id.order_line.search(
                    [('product_id', '=', order.product_id.id)], limit=1)
                if line:
                    order.sale_line_id = line.id

    # Set sale reference if production created from sale
    @api.model
    def create(self, vals):
        if vals.get('origin'):
            order = self.env['sale.order'].sudo().search(
                [('name', '=', vals.get('origin'))], limit=1)
            if order:
                vals['sale_id'] = order.id
            else:
                vals['sale_id'] = False
        return super(MRPProduction, self).create(vals)

    # Set sale reference if production created from sale
    def write(self, vals):
        if vals.get('origin'):
            order = self.env['sale.order'].sudo().search(
                [('name', '=', vals.get('origin'))], limit=1)
            if order:
                vals['sale_id'] = order.id
            else:
                vals['sale_id'] = False
        return super(MRPProduction, self).write(vals)
