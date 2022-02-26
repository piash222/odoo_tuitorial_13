from odoo import fields, models, api


class HospitalSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    note = fields.Char(string="Default Note")

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
