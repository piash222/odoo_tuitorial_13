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
