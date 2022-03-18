from odoo import fields, models, api


class HospitalSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    note = fields.Char(string="Default Note")
    # to download a module from settings
    # name should be module_technical_name_of_the_module
    module_crm = fields.Boolean(
        string='CRM',
        required=False)

    def set_values(self):
        res = super(HospitalSettings, self).set_values()
        print(self.note)
        self.env['ir.config_parameter'].set_param('om_hospital.note', self.note)
        return res

    @api.model
    def get_values(self):
        res = super(HospitalSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        note = ICPSudo.get_param('om_hospital.note')
        res.update(
            note=note
        )
        return res
