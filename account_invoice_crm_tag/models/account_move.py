# Copyright 2023 Tecnativa - Stefan Ungureanu
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    tag_ids = fields.Many2many(comodel_name="crm.tag", string="Invoice CRM tags")
