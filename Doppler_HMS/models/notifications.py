from odoo import api, fields, models, _


class HmsNotifications(models.Model):
    _name = "hms.notifications"
    _description = "Notifications Activity"

    name = fields.Char(string='Name', required=True, tracking=True)

