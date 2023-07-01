from odoo import api, fields, models, _


class HmsHKStatus(models.Model):
    _name = "hms.hk_status"
    _inherit = ['mail.thread']
    _description = "FO Status Activity"
    _rec_name = 'hk_status'

    hk_status = fields.Text(string='HK Status', required=True, tracking=True)
    date = fields.Date(string='Date', required=False, tracking=True)
    # ref = fields.Char(string="Reference", default=lambda self: _('New'))
