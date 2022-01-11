from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    @api.model
    def create(self, vals_list):
        if vals_list.get('name', _('New')) == _('New'):
            vals_list['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.seq') or _('New')
        return super(HospitalAppointment, self).create(vals_list)

    name = fields.Char(
        string='Appointment ID',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New'))

    def _get_default_patient(self):
        return 1

    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
        required=True,
        default=_get_default_patient)
    patient_age = fields.Integer(
        string='Age',
        related='patient_id.patient_age',
        required=False)
    appointment_date = fields.Date(
        string='Appointment Date',
        required=True)

    def _get_default_note(self):
        return "Subscribe"

    notes = fields.Text(
        string="Registration Note",
        required=False,
        default=_get_default_note)
