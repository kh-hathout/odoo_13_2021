# Copyright 2020 Jarsa Sistemas
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields
from odoo.tests import SavepointCase, tagged


@tagged("post_install", "-at_install")
class TestPurchaseStockOrderSecondaryUnit(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.warehouse = cls.env.ref("stock.warehouse0")
        cls.product_uom_kg = cls.env.ref("uom.product_uom_kgm")
        cls.product_uom_gram = cls.env.ref("uom.product_uom_gram")
        cls.product_uom_unit = cls.env.ref("uom.product_uom_unit")
        cls.product = cls.env["product.product"].create(
            {
                "name": "test",
                "type": "product",
                "uom_id": cls.product_uom_kg.id,
                "uom_po_id": cls.product_uom_kg.id,
                "secondary_uom_ids": [
                    (
                        0,
                        0,
                        {
                            "name": "unit-700",
                            "uom_id": cls.product_uom_unit.id,
                            "factor": 0.7,
                        },
                    )
                ],
            }
        )
        StockQuant = cls.env["stock.quant"]
        StockQuant.create(
            {
                "product_id": cls.product.id,
                "location_id": cls.warehouse.lot_stock_id.id,
                "quantity": 2000,
            }
        )
        cls.secondary_unit = cls.env["product.secondary.unit"].search(
            [("product_tmpl_id", "=", cls.product.product_tmpl_id.id)]
        )
        cls.product.purchase_secondary_uom_id = cls.secondary_unit.id
        cls.partner = cls.env["res.partner"].create({"name": "test - partner"})
        po = cls.env["purchase.order"].new(
            {
                "partner_id": cls.partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "name": cls.product.name,
                            "product_id": cls.product.id,
                            "product_qty": 1,
                            "product_uom": cls.product.uom_id.id,
                            "price_unit": 1000.00,
                            "date_planned": fields.Datetime.now(),
                        },
                    )
                ],
            }
        )
        po.onchange_partner_id()
        cls.order = cls.env["purchase.order"].create(po._convert_to_write(po._cache))

    def test_stock_move_line_secondary_unit(self):
        self.order.order_line.write(
            {"secondary_uom_id": self.secondary_unit.id, "secondary_uom_qty": 5}
        )
        self.order.order_line._onchange_secondary_uom()
        self.order.button_confirm()
        picking = self.order.picking_ids
        self.assertEqual(picking.move_line_ids.secondary_uom_qty, 5.0)
