from odoo import api, fields, models, _
from ast import literal_eval

class HmsReservation(models.Model):
    _name = "hms.reservation"
    _inherit = 'mail.thread'
    _description = "Reservation Activity"
    _rec_name = 'guest_name'

    ref = fields.Char(string="Reference", default=lambda self: _('Quick Reservation Form'))
    guest_name = fields.Char(string="Guest Name", required=True, tracking=True)
    arrival = fields.Date(string="Arrival", required=True, tracking=True)
    departure = fields.Date(string='Departure', required=True, tracking=True)
    adult = fields.Integer(string="Adult", required=True, tracking=True)
    rate_id = fields.Many2one('hms.room_status', string="Rate (Rs.)", tracking=True)
    room_types_id = fields.Many2one('hms.room_types', string="Room Types", required=True,
                                    tracking=True)
    agent = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Agent", tracking=True)
    room_ids = fields.Many2many('hms.room_status', 'reservation_room_rel', 'reservation_id', 'room_id', string="Rooms",
                                required=True, tracking=True)

    box = fields.Char(string="Box")
    header = fields.Char(string="Header")
    arrival_img = fields.Image("Student Image")

    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    room_summary = fields.Html(string="Room Summary")
    color = fields.Integer(string="Color")
    name = fields.Char('Operation Type', required=True, translate=True)

    count_picking_draft = fields.Integer(compute='_compute_picking_count')
    count_arrival = fields.Integer(compute='_compute_arrival_count')
    count_picking = fields.Integer(compute='_compute_picking_count')
    count_picking_waiting = fields.Integer(compute='_compute_picking_count')
    count_picking_late = fields.Integer(compute='_compute_picking_count')
    count_picking_backorders = fields.Integer(compute='_compute_picking_count')
    hide_reservation_method = fields.Boolean(compute='_compute_hide_reservation_method')

    def name_get(self):
        res = []
        for rec in self:
            date = f'{rec.arrival}  - {rec.departure}'
            res.append((rec.id, date))
        return res

    @api.onchange('room_types_id')
    def onchange_room_type(self):
        if self.room_types_id:
            # Assuming you have a model for room statuses called 'hms.room_status'
            room_statuses = self.env['hms.room_status'].search([
                ('room_types_id', '=', self.room_types_id.id),
                ('fo_status_id.fo_status', '=', 'Vacant')
            ])
            room_ids = room_statuses.mapped('room_no')
            domain = [('room_no', 'in', room_ids)]
            return {'domain': {'room_ids': domain}}
        else:
            self.room_ids = False

    @api.model
    def create(self, vals):
        reservation = super(HmsReservation, self).create(vals)
        reservation._update_room_statuses()
        return reservation

    def write(self, vals):
        res = super(HmsReservation, self).write(vals)
        self._update_room_statuses()
        return res

    def _update_room_statuses(self):
        occupied_status = self.env['hms.fo_status'].search([('fo_status', '=', 'Reserved')], limit=1)
        if occupied_status:
            for reservation in self:
                room_statuses = self.env['hms.room_status'].search([
                    ('room_no', 'in', reservation.room_ids.mapped('room_no')),
                ])
                room_statuses.write({'fo_status_id': occupied_status.id})


    def get_stock_picking_action_picking_type(self):
        return self._get_action('stock.stock_picking_action_picking_type')

    def get_action_picking_tree_ready(self):
        return self._get_action('stock.action_picking_tree_ready')

    def get_action_reservation_ready(self):
        return self.get_action('hms.action_reservation_ready')

    def _get_action(self, action_xmlid):
        action = self.env["ir.actions.actions"]._for_xml_id(action_xmlid)
        if self:
            action['display_name'] = self.display_name

        context = {
            'search_default_arrival': [self.id],
            'default_arrival': self.id,
        }

        action_context = literal_eval(action['context'])
        context = {**action_context, **context}
        action['context'] = context
        return action