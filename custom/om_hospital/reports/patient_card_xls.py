from odoo import fields, models, api


class PatientCardXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, objs):
        print(objs)
        sheet = workbook.add_worksheet("Patient card")
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet.write(2, 2, 'name', format1)
        sheet.write(2, 3, objs.patient_name, format2)
