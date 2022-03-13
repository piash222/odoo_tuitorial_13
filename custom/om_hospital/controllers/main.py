from odoo import http
from odoo.http import request


class Hospital(http.Controller):

    # sample controller created
    # auth='user' >> webpage visible for authenticated logged in user
    # auth='public' >> webpage visible for all including not logged in
    @http.route('/hospital/patient/', website=True, auth='public')
    def hospital_patient(self):
        patients = request.env['hospital.patient'].sudo().search([])
        print(patients)
        # return "Hello World"
        return request.render('om_hospital.patient_page', {'patients': patients})

    @http.route('/get_patients', type='json', auth='user')
    def get_patients(self):
        patients_rec = request.env['hospital.patient'].search([])
        patients = []
        for rec in patients_rec:
            vals = {
                'id': rec.id,
                'name': rec.patient_name
            }
            patients.append(vals)
        data = {
            'status': 200, 'response': patients, 'message': 'success'
        }
        return data

    @http.route("/create_patients",type='json', auth='user')
    def create_patients(self, **rec):
        if request.jsonrequest:
            print("rec", rec)
            if rec["name"]:
                vals = {
                    'patient_name': rec['name']
                }
                new_patient = request.env['hospital.patient'].sudo().create(vals)
                args = {"success": True, "ID": new_patient.id}
            return args
