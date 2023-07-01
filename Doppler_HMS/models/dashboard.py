from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HmsDashboard(models.Model):
    _name = "hms.dashboard"
    _inherit = 'mail.thread'
    _description = "Dashboard Activity"
    # _inherit = 'hms.reservation'
    # _rec_name = 'ref'

    name = fields.Char(string='Name', required=True, tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New Data from Dashboard'))
    first_name = fields.Char(string='First Name', required=True, tracking=True)
    room_types_id = fields.Many2one('hms.room_types', string="Room Types", required=True, tracking=True)

    # reservation_first_name = fields.Char(string='Reservation First Name', related='reservation_id.first_name')
    reservation_id = fields.Many2one('hms.reservation', string="Reservation",
                                     ref="Doppler_HMS.view_hms_reservation_tree", required=True, tracking=True)

    # room_status_fields = fields.Many2one('hms.room_status', string="Room Status")
    # model_one_id = fields.Many2one('model.one', string="Model One")
    # reservations_id = fields.Many2one('hms.reservation', string="Reservation")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hotel.reservation')
        return super(HmsDashboard, self).create(vals_list)

# class ReservationInherit(models.Model):
#     _inherit = 'hms.reservation'
#
#     first_name = fields.Char(string='First Name', required=False, tracking=True)
# title = fields.Text(string='Title', required=True, tracking=True)
