from odoo import fields, models, api


class HospitalPatient (models.Model):
    _name = 'hospital.patient'
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
