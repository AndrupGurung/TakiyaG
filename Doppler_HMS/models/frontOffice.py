from odoo import api, fields, models, _


class HmsFrontOffice(models.Model):
    _name = "hms.front_office"
    _description = "Front Office Activity"

    name = fields.Char(string='Name', required=True, tracking=True)

