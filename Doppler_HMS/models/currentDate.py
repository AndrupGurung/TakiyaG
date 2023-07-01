from odoo import api, fields, models, _


class HmsCurrentDate(models.Model):
    _name = "hms.current_date"
    _inherit = 'mail.thread'
    _description = "Current Date Activity"

    #name = fields.Char(string='Name', required=True, tracking=True)
    #date_today = fields.Date(string='Today\'s Date', compute='_compute_date_today')


    #@api.depends('date_today')
    #def _compute_date_today(self):
     #   for record in self:
     #       record.date_today = fields.Date.today()

