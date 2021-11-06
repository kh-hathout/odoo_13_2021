# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, exceptions, api, _
from datetime import datetime
from odoo.exceptions import Warning ,ValidationError, UserError

        
        

class MassConfirmPicking(models.TransientModel):
    _name = 'mass.confirm.picking'
    _description = 'Mass Confirm Picking'

    
   
    def action_confirm_picking(self):
        
        if self._context.get('active_model') == 'stock.picking':
            active_ids = self._context.get('active_ids')
            pickings = self.env['stock.picking'].browse(active_ids)
            if pickings:
                pick_to_do = self.env['stock.picking']
                for picking in pickings: 
                    picking.button_validate()
                    # If still in draft => confirm and assign
                    if picking.state == 'draft':
                        picking.action_confirm()
                        if picking.state != 'assigned':
                            picking.action_assign()
                            if picking.state != 'assigned':
                                raise UserError(_("Could not reserve all requested products. Please use the \'Mark as Todo\' button to handle the reservation manually."))
                    for move in picking.move_lines.filtered(lambda m: m.state not in ['done', 'cancel']):
                        for move_line in move.move_line_ids:
                            move_line.qty_done = move_line.product_uom_qty
                    pick_to_do |= picking
                    if pick_to_do:
                        pick_to_do.action_done()
            
            
            
            
        
        if self._context.get('active_model') == 'sale.order':
            active_ids = self._context.get('active_ids')
            so_obj = self.env['sale.order'].browse(active_ids)
            so_not_confirm = so_obj.search([('state', 'not in', ['sale']), ('id', 'in', active_ids)]).mapped('name')
            if any(obj.state != 'sale' for obj in so_obj):
                raise UserError(_(' %s Record(s) is not in confirm state. Please confirm it.')% (so_not_confirm))
            else:
                pickings = self.env['stock.picking'].search([('sale_id', 'in', active_ids), ('state', 'not in', ['done','cancel']), ('state', 'in', ['confirmed'])])
                if pickings:
                    for picking in pickings: 
                        picking.button_validate()
                
                pickings = self.env['stock.picking'].search([('sale_id', 'in', active_ids), ('state', 'not in', ['done','cancel']), ('state', 'in', ['assigned'])])
                if pickings:
                    pick_to_do = self.env['stock.picking']
                    for picking in pickings: 
                        picking.button_validate()
                        # If still in draft => confirm and assign
                        if picking.state == 'draft':
                            picking.action_confirm()
                            if picking.state != 'assigned':
                                picking.action_assign()
                                if picking.state != 'assigned':
                                    raise UserError(_("Could not reserve all requested products. Please use the \'Mark as Todo\' button to handle the reservation manually."))
                        for move in picking.move_lines.filtered(lambda m: m.state not in ['done', 'cancel']):
                            for move_line in move.move_line_ids:
                                move_line.qty_done = move_line.product_uom_qty
                        pick_to_do |= picking
                        if pick_to_do:
                            pick_to_do.action_done()
                        
        if self._context.get('active_model') == 'purchase.order':
            active_ids = self._context.get('active_ids')
            po_obj = self.env['purchase.order'].browse(active_ids)
            
            po_not_confirm = po_obj.search([('state', 'not in', ['purchase']), ('id', 'in', active_ids)]).mapped('name')
            if any(obj.state != 'purchase' for obj in po_obj):
                raise UserError(_(' %s Record(s) is not in confirm state. Please confirm it.')% (po_not_confirm))
            else:
                pickings = self.env['stock.picking'].search([('purchase_id', 'in', active_ids), ('state', 'not in', ['done','cancel']), ('state', 'in', ['confirmed'])])
                if pickings:
                    for picking in pickings: 
                        picking.button_validate()
                
                pickings = self.env['stock.picking'].search([('purchase_id', 'in', active_ids), ('state', 'not in', ['done','cancel']), ('state', 'in', ['assigned'])])
                if pickings:
                    pick_to_do = self.env['stock.picking']
                    for picking in pickings: 
                        picking.button_validate()
                        # If still in draft => confirm and assign
                        if picking.state == 'draft':
                            picking.action_confirm()
                            if picking.state != 'assigned':
                                picking.action_assign()
                                if picking.state != 'assigned':
                                    raise UserError(_("Could not reserve all requested products. Please use the \'Mark as Todo\' button to handle the reservation manually."))
                        for move in picking.move_lines.filtered(lambda m: m.state not in ['done', 'cancel']):
                            for move_line in move.move_line_ids:
                                move_line.qty_done = move_line.product_uom_qty
                        pick_to_do |= picking
                        if pick_to_do:
                            pick_to_do.action_done()
        return True
    

            
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
