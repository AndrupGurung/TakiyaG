from odoo import api, fields, models, _


class HmsRoomStatus(models.Model):
    _name = "hms.room_status"
    _inherit = ['mail.thread']
    _description = "Room Status Activity"
    _rec_name = 'room_no'

    room_no = fields.Integer(string='Room No', required=True, tracking=True)
    room_types_id = fields.Many2one('hms.room_types', string="Room Types", tracking=True)
    features_id = fields.Many2one('hms.room_features', string="Features", tracking=True)
    fo_status_id = fields.Many2one('hms.fo_status', string="FO Status", tracking=True)
    hk_status_id = fields.Many2one('hms.hk_status', string="HK Status", tracking=True)

    rate = fields.Text(string="Rate (Rs.)", required=True, tracking=True)
    date = fields.Date(string='Booked Date', required=False, tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New Room Information'))

    # reservation_ids = fields.Many2many('hms.reservation', string="Booked Date",
    #                                    required=True, tracking=True, compute='_compute')

    # def name_get(self):
    #     res = []
    #     for rec in self:
    #         name = f'{rec.name}  - {rec.ref}'
    #         res.append((rec.id, name))
    #     return res
