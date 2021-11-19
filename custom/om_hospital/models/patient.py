from odoo import fields, models, api


class HospitalPatient (models.Model):
    _name = 'hospital.patient'
    _description = 'Patient records'

    patient_name = fields.Char(
        string="Name",
        required=True)

    patient_age = fields.Char(
        string='Age',
        required=False)

    notes = fields.Text(
        string="Notes",
        required=False)
    Image = fields.Binary(string="Image")
