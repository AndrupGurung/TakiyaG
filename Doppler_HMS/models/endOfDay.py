from odoo import api, fields, models, _


class HmsEndOfDay(models.Model):
    _name = "hms.end_of_day"
    _description = "End of Day Activity"

    name = fields.Char(string='Name', required=True, tracking=True)
