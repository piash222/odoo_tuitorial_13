from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(
        string='Patient Name',
        required=False)


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient records'
    _rec_name = 'patient_name'

    patient_name = fields.Char(
        string="Name",
        tracking=True,
        required=True)

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError(_("Age must be greater than 5"))

    patient_age = fields.Integer(
        string='Age',
        tracking=True,
        required=False, )

    notes = fields.Text(
        string="Notes",
        required=False)
    image = fields.Binary(string="Image")
    name = fields.Char(string='Test')
    name_seq = fields.Char(string='name sequence',
                           required=True,
                           copy=False,
                           readonly=True,
                           index=True,
                           default=lambda self: _('New'))

    patient_gender = fields.Selection(
        string='Patient Gender',
        selection=[('male', 'Male'),
                   ('fe_male', 'Female'), ],
        required=False)

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age < 18:
                rec.age_group = 'minor'
            else:
                rec.age_group = 'major'

    age_group = fields.Selection(
        string='Age Group',
        selection=[('major', 'Major'),
                   ('minor', 'Minor'), ],
        required=False, compute='set_age_group')

    appointment_count = fields.Integer(
        string='Appointment count',
        compute='_get_appointment_count')

    def _get_appointment_count(self):
        self.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])

    def patient_appointment(self):
        return {
            'name': _('appointments'),
            'res_model': 'hospital.appointment',
            'view_mode': 'tree,form',
            'domain': [("patient_id", '=', self.id)],
            'type': 'ir.actions.act_window'

        }

    @api.model
    def create(self, values):
        if values.get('name_seq', _('New')) == _('New'):
            values['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.seq') or _('New')
        return super(HospitalPatient, self).create(values)
