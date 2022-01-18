from odoo import fields, models, api


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Information'

    name = fields.Char(required=True)
    doctor_gender = fields.Selection(
        string='Doctor Gender',
        selection=[('male', 'Male'),
                   ('fe_male', 'Female'), ], )
    related_user = fields.Many2one(
        comodel_name='res.users',
        string='Related User',
        required=False)
