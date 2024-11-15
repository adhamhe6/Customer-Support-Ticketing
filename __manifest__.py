{
    'name': 'Customer Support Ticketing System',
    'version': '1.0',
    'category': 'Customer Service',
    'summary': 'Manage customer support tickets',
    'author': 'Your Name',
    'depends': ['mail'],  # Depends on mail module for email notifications
    'data': [
        'security/security.xml',
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/ticket_views.xml',
        'views/ticket_templates.xml',
    ],
    'installable': True,
    'application': True,
}
