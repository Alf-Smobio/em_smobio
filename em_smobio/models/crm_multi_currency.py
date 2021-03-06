# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, models, fields


class CRMLeadInherit(models.Model):
    _inherit = ['crm.lead']

    currency_id = fields.Many2one('res.currency', string='Moneda', tracking=True)
