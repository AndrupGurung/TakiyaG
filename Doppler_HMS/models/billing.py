from odoo import api, fields, models, _


class HmsBilling(models.Model):
    _name = "hms.billing"
    _description = "Billing Activity"

    name = fields.Char(string='Name', required=True, tracking=True)
