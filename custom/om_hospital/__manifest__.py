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
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/patient_seq.xml',
        'data/data.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctors.xml',
        'wizards/create_appointment.xml',
        'reports/reports.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
