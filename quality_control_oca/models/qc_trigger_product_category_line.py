# Copyright 2010 NaN Projectes de Programari Lliure, S.L.
# Copyright 2014 Serv. Tec. Avanzados - Pedro M. Baeza
# Copyright 2014 Oihane Crucelaegui - AvanzOSC
# Copyright 2017 ForgeFlow S.L.
# Copyright 2017 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class QcTriggerProductCategoryLine(models.Model):
    _inherit = "qc.trigger.line"
    _name = "qc.trigger.product_category_line"
    _description = "Quality Control Trigger Product Category Line"

    product_category = fields.Many2one(comodel_name="product.category")
    def get_trigger_line_for_product(self, trigger, product, partner=False):
        trigger_lines = super().get_trigger_line_for_product(
            trigger, product, partner=partner
        )
        category = product.categ_id
        while category:
            for trigger_line in category.qc_triggers.filtered(
                lambda r: r.trigger == trigger
                and (
                    not r.partners
                    or not partner
                    or partner.commercial_partner_id in r.partners
                )
            ):
                trigger_lines.add(trigger_line)
            category = category.parent_id
        return trigger_lines
