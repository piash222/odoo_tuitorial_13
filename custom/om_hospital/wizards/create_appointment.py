from odoo import fields, models, api


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'

    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
        required=True)
    appointment_date = fields.Date(
        string='Appointment Date',
        required=True)

    def create_appointment(self):

        vals = {
            'patient_id':self.patient_id.id,
            'appointment_date': self.appointment_date
        }
        self.env['hospital.appointment'].create(vals)
