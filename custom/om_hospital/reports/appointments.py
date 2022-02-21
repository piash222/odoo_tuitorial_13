from odoo import fields, models, api


class ModelName(models.AbstractModel):
    _name = 'report.om_hospital.report_appointment_view'
    _description = 'Appointment Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('docids', docids)
        if data['form']['patient_id'][0]:
            selected_patient = data['form']['patient_id'][0]
            appointments = self.env['hospital.appointment'].search([('patient_id', '=', selected_patient)])
        else:
            appointments = self.env['hospital.appointment'].search([])
        data['docs'] = appointments
        return {
            'doc_ids': docids,
            'data': data,
            'docs': data['docs'],
        }

