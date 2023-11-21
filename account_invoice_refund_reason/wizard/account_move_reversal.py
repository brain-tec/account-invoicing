# Copyright (C) 2019 Open Source Integrators
# Copyright (C) 2019 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class AccountMoveReversal(models.TransientModel):
    _inherit = "account.move.reversal"

    reason_id = fields.Many2one("account.move.refund.reason", string="Refund Reason")
    reason = fields.Char(
        compute="_compute_reason", precompute=True, store=True, readonly=False
    )

    @api.depends("reason_id")
    def _compute_reason(self):
        for record in self:
            if record.reason_id:
                record.reason = record.reason_id.name

    def reverse_moves(self):
        """Overriden to set the reason_id fields in the new created refunds"""
        res = super().reverse_moves()
        if "res_id" in res:
            if (
                self.refund_method == "modify"
            ):  # When modify, res_id contains the new invoice and not the refund
                refunds = self.move_ids.mapped("reversal_move_id").sorted("id")[-1:]
            else:
                refunds = self.move_ids.mapped("reversal_move_id").filtered(
                    lambda r: r.id == res["res_id"]
                )
        elif "domain" in res:
            refunds = self.move_ids.mapped("reversal_move_id").filtered_domain(
                res["domain"]
            )
        else:
            refunds = self.move_ids.mapped("reversal_move_id")
        refunds.write({"reason_id": self.reason_id.id})
        return res
