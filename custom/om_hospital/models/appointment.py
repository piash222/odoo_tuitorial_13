from odoo import models, fields, api, _
import pytz


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    @api.model
    def create(self, vals_list):
        if vals_list.get('name', _('New')) == _('New'):
            vals_list['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.seq') or _('New')
        return super(HospitalAppointment, self).create(vals_list)

    def write(self, values):
        # Add code here
        result = super(HospitalAppointment, self).write(values)
        print("test write function")
        return result

    name = fields.Char(
        string='Appointment ID',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New'))

    def _get_default_patient(self):
        return 1

    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
        required=True,
        default=_get_default_patient)
    patient_age = fields.Integer(
        string='Age',
        related='patient_id.patient_age',
        required=False)
    appointment_date = fields.Datetime(
        string='Appointment Date',
        required=True)

    def _get_default_note(self):
        return "Subscribe"

    notes = fields.Text(
        string="Registration Note",
        required=False,
        default=_get_default_note)

    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancel', 'Cancel')],
        default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    doctor_note = fields.Char(
        string='Doctor Note',
        required=False)
    pharmacy_note = fields.Char(
        string='Pharmacy Note',
        required=False)
    active = fields.Boolean(
        string='Active',
        related='patient_id.active',
        required=False)
    appointment_lines = fields.One2many(
        comodel_name='hospital.appointment.lines',
        inverse_name='appointment_id',
        string='Appointment_lines',
        required=False)

    @api.model
    def default_get(self, fields_list):
        res = super(HospitalAppointment, self).default_get(fields_list)
        res['patient_id'] = 2
        res['notes'] = "Default note from default get function"
        return res

    def delete_lines(self):
        for rec in self:
            print("Time in UTC,", rec.appointment_date)
            user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
            print(user_tz, type(user_tz))
            time_local = pytz.utc.localize(rec.appointment_date).astimezone(user_tz)
            print(time_local)
            rec.appointment_lines = [(5, 0, 0)]

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner Id',
        required=False)

    # domain using onchange method

    # @api.onchange('partner_id')
    # def _onchange_partner_id(self):
    #     for rec in self:
    #         rec.order_id = None
    #         return {
    #             'domain':
    #                 {'order_id': [('partner_id', '=', rec.partner_id.id)]}
    #         }

    # domain using field domain
    order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Order Id',
        required=False, domain="[('partner_id', '=', partner_id)]")


class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        required=False)
    product_qty = fields.Integer(
        string='Quantity',
        required=False)
    appointment_id = fields.Many2one(
        comodel_name='hospital.appointment',
        string='Appointment Id',
        required=False)
