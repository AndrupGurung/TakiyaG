from odoo import api, fields, models, _


class HmsLogOut(models.Model):
    _name = "hms.log_out"
    _description = "Log Out Activity"

    name = fields.Char(string='Name', required=True, tracking=True)
