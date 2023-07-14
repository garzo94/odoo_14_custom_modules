from odoo import api, fields, models, _

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True, translate=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done'), ('cancel', 'Cancelled')],
                             string='Status', default="draft", tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Responsable")
    def action_draft(self):
        self.state = "draft"

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_cancel(self):
        self.state = "cancel"
    @api.model
    def create(self,vals):
        print(vals,"-------")
        if not vals.get("note"):
            vals["note"] = "New patient"
        return super(HospitalPatient, self).create(vals)
