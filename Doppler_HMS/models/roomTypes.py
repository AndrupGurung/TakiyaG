from odoo import api, fields, models, _


class HmsRoomTypes(models.Model):
    _name = "hms.room_types"
    _inherit = ['mail.thread']
    _description = "Room Types Activity"
    _rec_name = 'room_types'

    # name = fields.Char(string='Room Name', required=True, tracking=True)
    room_types = fields.Text(string='Room Types', required=True, tracking=True)
    date = fields.Date(string='Date', required=False, tracking=True)
