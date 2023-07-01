from odoo import api, fields, models, _
from ast import literal_eval

class HmsReports(models.Model):
    _name = "hms.reports"
    _description = "Reports Activity"

    name = fields.Char('Operation Type', required=True, translate=True)
    color = fields.Integer('Color')
    arrival = fields.Char(string='Arrival', required=True, tracking=True)
    departure = fields.Char(string='Departure', required=True, tracking=True)
    inhouse = fields.Char(string='In-House', required=True, tracking=True)
    roommanage = fields.Char(string='Room Management', required=True, tracking=True)
    code = fields.Selection([('incoming', 'Arrival'), ('outgoing', 'Departure'), ('internal', 'In-House')],
                            'Type of Operation', required=True)
    reserve_id = fields.Many2one(
      'hms.reservation', 'Reservation', compute='_compute_reserve_id', store=True, readonly=False, ondelete='cascade')

    @api.depends('arrival', 'departure')
    def _compute_reserve_id(self):
        for record in self:
            record.reserve_id = str(record.arrival) + ' - ' + str(record.departure)

    def get_reports_action_picking_type(self):
        return self._get_action('reports.reports_action_picking_type')

    def get_action_picking_tree_ready(self):
        return self._get_action('stock.action_picking_tree_ready')

    def get_action_reports_ready(self):
        return self.get_action('hms.action_reports_ready')

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





