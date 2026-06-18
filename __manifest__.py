{
        'name': 'Log - Incident Resolution',
        'version': '17.0.1.0.0',
        'summary': 'Registro de incidencias y resolucion de tareas tecnicas',
        'depends': ['project'],
        'data': [
                'security/ir.model.access.csv',
                'views/log_incident_views.xml',
        ],
        'installable': True,
        'application': True,
}