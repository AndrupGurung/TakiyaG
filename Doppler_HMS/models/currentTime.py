from odoo import api, fields, models, _


class HmsCurrentTime(models.Model):
    _name = "hms.current_time"
    _description = "Current Time Activity"

    name = fields.Char(string='Name', required=True, tracking=True)
