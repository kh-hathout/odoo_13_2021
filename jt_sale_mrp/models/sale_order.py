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


class SaleOderdata(models.Model):
    _inherit = 'sale.order'

    def _compute_production_count(self):
        for order in self:
            order.production_count = len(order.production_ids.ids)

    production_count = fields.Integer(
        string="Manufacturing Orders", compute="_compute_production_count")
    production_ids = fields.One2many(
        'mrp.production', 'sale_id', string='Productions')

    @api.depends('production_ids.state')
    def _compute_mrp_state(self):
        for order in self:
            production_states = order.production_ids.mapped('state')
            if 'draft' in production_states:
                order.mrp_state = 'draft'
            elif 'confirmed' in production_states:
                order.mrp_state = 'confirmed'
            elif 'planned' in production_states:
                order.mrp_state = 'planned'
            elif 'progress' in production_states:
                order.mrp_state = 'progress'
            elif 'to_close' in production_states:
                order.mrp_state = 'to_close'
            elif 'done' in production_states:
                order.mrp_state = 'done'
            elif 'cancel' in production_states:
                order.mrp_state = 'cancel'
            else:
                order.mrp_state = 'draft'

    mrp_state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('planned', 'Planned'),
        ('progress', 'In Progress'),
        ('to_close', 'To Close'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string='MRP Orders Status',
        compute='_compute_mrp_state', store=True)

    # Action open manufacturing orders
    def action_open_mrp_production_view(self):
        action = self.env.ref('mrp.mrp_production_action').read()[0]
        action['name'] = "Manufacturing Orders"
        action['domain'] = [('sale_id', '=', self.id)]
        action['context'] = {'default_sale_id': self.id}
        return action


class SalesOrderLine(models.Model):

    _inherit = 'sale.order.line'

    def view_mrp_orders(self):
        action = self.env.ref('mrp.mrp_production_action').read()[0]
        action['name'] = "Manufacturing Orders"
        action['domain'] = [('sale_line_id', '=', self.id)]
        action['context'] = {'default_sale_line_id': self.id}
        return action

    def _compute_count_mrp(self):
        for line in self:
            line.count_mrp = self.env['mrp.production'].sudo(
            ).search_count([('sale_line_id', '=', line.id)])

    count_mrp = fields.Integer(string='MRP Orders',
                               compute="_compute_count_mrp")
