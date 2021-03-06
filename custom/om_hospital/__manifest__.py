{
    'name': 'Hospital Management',
    'version': '13.0.1.0.0',
    'summary': 'Module for managing the Hospital',
    'description': 'Description',
    'sequence': '10',
    'category': 'Extra Tools',
    'author': 'Md. Shihab Uddin',
    'website': 'Website',
    'license': 'LGPL-3',
    'depends': [
        'mail',
        'sale',
        'report_xlsx',
        'sale_stock',
        'website'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/patient_seq.xml',
        'data/data.xml',
        'data/cron_job_data.xml',
        'wizards/create_appointment.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctors.xml',
        'views/template.xml',
        'views/settings.xml',
        'reports/reports.xml',
        'reports/sale_report_inherit.xml',
        'reports/appointment.xml',
        'data/mail_template.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
