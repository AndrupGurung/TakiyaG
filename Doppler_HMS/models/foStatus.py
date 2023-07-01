from odoo import api, fields, models, _


class HmsFOStatus(models.Model):
    _name = "hms.fo_status"
    _inherit = ['mail.thread']
    _description = "FO Status Activity"
    _rec_name = 'fo_status'

    fo_status = fields.Text(string='FO Status', required=True, tracking=True)
    date = fields.Date(string='Date', required=False, tracking=True)
    # ref = fields.Char(string="Reference", default=lambda self: _('New'))
