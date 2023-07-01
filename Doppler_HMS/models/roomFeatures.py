from odoo import api, fields, models, _


class HmsRoomFeatures(models.Model):
    _name = "hms.room_features"
    _inherit = ['mail.thread']
    _description = "Room Features Activity"
    _rec_name = 'features'

    features = fields.Text(string='Features', required=True, tracking=True)
    date = fields.Date(string='Date', required=False, tracking=True)
    # ref = fields.Char(string="Reference", default=lambda self: _('New'))
