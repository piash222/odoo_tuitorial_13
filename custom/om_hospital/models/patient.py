from odoo import fields, models, api, _


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
        required=True)

    patient_age = fields.Char(
        string='Age',
        required=False)

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


    @api.model
    def create(self, values):
        if values.get('name_seq', _('New')) == _('New'):
            values['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.seq') or _('New')
        return super(HospitalPatient, self).create(values)
