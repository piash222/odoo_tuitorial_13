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
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date
        }
        self.patient_id.message_post(body="appointment created successfully", subject="Appointment Creation")
        self.env['hospital.appointment'].create(vals)

    def get_data(self):
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', 2)])
        for rec in appointments:
            print("appointment Name", rec.name)
        print('appointments', appointments)
        return {
            'type': 'ir.actions.do_nothing'
        }

    def delete_patient(self):
        self.patient_id.unlink()

    def patient_print(self):
        # print('read', self.read())
        # print('patient_id', self.patient_id)
        # print('appointment_date', self.appointment_date)
        data = {
            'model': 'hospital.appointment',
            'form': self.read()[0]
        }
        # if data['form']['patient_id'][0]:
        #     selected_patient = data['form']['patient_id'][0]
        #     appointments = self.env['hospital.appointment'].search([('patient_id', '=', selected_patient)])
        # else:
        #     appointments = self.env['hospital.appointment'].search([])
        # data['docss'] = appointments
        # print(appointments)
        # print('data', data)
        return self.env.ref('om_hospital.report_appointment').report_action(self, data=data)
