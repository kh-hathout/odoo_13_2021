# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.tools.float_utils import float_round as round
from odoo.addons import decimal_precision as dp

# add Secondary UOM and Secondary Qty field in bom line with compute uom

class MRPSecUOMbomline(models.Model):
	_inherit = 'mrp.bom.line'

	secondary_uom_id = fields.Many2one('uom.uom', compute='_mrp_quantity_secondary_compute', string="Secondary UOM", store=True)
	secondary_quantity = fields.Float('Secondary Qty', compute='_mrp_quantity_secondary_compute', digits=dp.get_precision('Product Unit of Measure'), store=True)

	@api.depends('product_id', 'product_qty')
	def _mrp_quantity_secondary_compute(self):
		for order in self:
			if order.product_id.is_secondary_uom:
				uom_quantity = order.product_id.uom_id._compute_quantity(order.product_qty, order.product_id.secondary_uom_id, rounding_method='HALF-UP')
				order.secondary_uom_id = order.product_id.secondary_uom_id
				order.secondary_quantity = uom_quantity	

# add  Secondary UOM,Secondary Qty,Secondary Reserved Qty and Secondary Consumed Qty fields in mrp order  line with compute uom

class MRPSmodel(models.Model):
	_inherit = 'mrp.production'
	secondary_uom_id = fields.Many2one('uom.uom',string="Secondary UOM")
	_inherit = 'stock.move'

	secondary_uom_id = fields.Many2one('uom.uom', compute='_quantity_secondary_compute', string="Secondary UOM", store=True)
	secondary_quantity = fields.Float('Secondary Qty', compute='_quantity_secondary_compute', digits=dp.get_precision('Product Unit of Measure'), store=True)

	secondary_quantity_reserved = fields.Float('Secondary Reserved Qty', compute='_reserved_secondary_compute', digits=dp.get_precision('Product Unit of Measure'), store=True)
	secondary_quantity_done = fields.Float('Secondary Consumed Qty', compute='_quantity_done_econdary_compute', digits=dp.get_precision('Product Unit of Measure'), store=True)

	@api.depends('product_id', 'product_uom_qty')
	def _quantity_secondary_compute(self):
		for order in self:
			if order.product_id.is_secondary_uom:
				uom_quantity = order.product_id.uom_id._compute_quantity(order.product_uom_qty, order.product_id.secondary_uom_id, rounding_method='HALF-UP')
				order.update({'secondary_uom_id' : order.product_id.secondary_uom_id})
				order.update({'secondary_quantity' : uom_quantity})
			else:
				order.update({'secondary_uom_id' : False})
				order.update({'secondary_quantity' : 0.0})

	@api.depends('product_id', 'reserved_availability')
	def _reserved_secondary_compute(self):
		for order in self:
			if order.product_id.is_secondary_uom:
				uom_quantity = order.product_id.uom_id._compute_quantity(order.reserved_availability, order.product_id.secondary_uom_id, rounding_method='HALF-UP')
				order.update({'secondary_uom_id' : order.product_id.secondary_uom_id})
				order.update({'secondary_quantity_reserved' : uom_quantity})
			else:
				order.update({'secondary_uom_id' : False})
				order.update({'secondary_quantity_reserved' : 0.0})

	@api.depends('product_id', 'quantity_done')
	def _quantity_done_econdary_compute(self):
		for order in self:
			if order.product_id.is_secondary_uom:
				uom_quantity = order.product_id.uom_id._compute_quantity(order.quantity_done, order.product_id.secondary_uom_id, rounding_method='HALF-UP')
				order.update({'secondary_uom_id' : order.product_id.secondary_uom_id})
				order.update({'secondary_quantity_done' : uom_quantity})
			else:
				order.update({'secondary_uom_id' : False})
				order.update({'secondary_quantity_done' : 0.0})


	
# add  Secondary UOM,Secondary Qty,Secondary Reserved Qty and Secondary Consumed Qty fields in Produce wizard with compute uom


class productproducewizard(models.TransientModel):
	_inherit = 'mrp.product.produce.line'

	secondary_uom_id = fields.Many2one('uom.uom', compute='_quantity_secondary_compute', string="Secondary UOM", store=True)
	secondary_quantity = fields.Float('Secondary Qty', compute='_quantity_secondary_compute', digits=dp.get_precision('Product Unit of Measure'), store=True)
	
	secondary_quantity_reserved = fields.Float('Secondary Reserved Qty', compute='_reserved_secondary_compute', digits=dp.get_precision('Product Unit of Measure'), store=True)
	secondary_quantity_done = fields.Float('Secondary Consumed Qty', compute='_quantity_done_econdary_compute', digits=dp.get_precision('Product Unit of Measure'), store=True)
	
	@api.depends('product_id', 'qty_to_consume')
	def _quantity_secondary_compute(self):
		for order in self:
			if order.product_id.is_secondary_uom:
				uom_quantity = order.product_id.uom_id._compute_quantity(order.qty_to_consume, order.product_id.secondary_uom_id, rounding_method='HALF-UP')
				order.update({'secondary_uom_id' : order.product_id.secondary_uom_id})
				order.update({'secondary_quantity' : uom_quantity})
			else:
				order.update({'secondary_uom_id' : False})
				order.update({'secondary_quantity' : 0.0})

	@api.depends('product_id', 'qty_reserved')
	def _reserved_secondary_compute(self):
		for order in self:
			if order.product_id.is_secondary_uom:
				uom_quantity = order.product_id.uom_id._compute_quantity(order.qty_reserved, order.product_id.secondary_uom_id, rounding_method='HALF-UP')
				order.update({'secondary_uom_id' : order.product_id.secondary_uom_id})
				order.update({'secondary_quantity_reserved' : uom_quantity})
			else:
				order.update({'secondary_uom_id' : False})
				order.update({'secondary_quantity_reserved' : 0.0})

	@api.depends('product_id', 'qty_done')
	def _quantity_done_econdary_compute(self):
		for order in self:
			if order.product_id.is_secondary_uom:
				uom_quantity = order.product_id.uom_id._compute_quantity(order.qty_done, order.product_id.secondary_uom_id, rounding_method='HALF-UP')
				order.update({'secondary_uom_id' : order.product_id.secondary_uom_id})
				order.update({'secondary_quantity_done' : uom_quantity})
			else:
				order.update({'secondary_uom_id' : False})
				order.update({'secondary_quantity_done' : 0.0})				