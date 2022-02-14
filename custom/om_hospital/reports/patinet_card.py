from odoo import api, models


class PatientCardReport(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_view'
    _description = "Patient Card Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        print(self, 'self')
        print(docids, 'docids')
        print(data, 'data')

        docs = self.env['hospital.patient'].browse(docids)
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        print(appointments)
        app_list = []
        for appointment in appointments:
            vals = {
                "patient": appointment.patient_id.patient_name,
                "date": appointment.appointment_date,
                'age': appointment.patient_age

            }
        app_list.append(vals)
        return {
            'doc_ids': docids,
            'data': data,
            'docs': docs,
            'appointment_list': app_list

        }
