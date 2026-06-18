from odoo import models, fields

class LogIncident(models.Model):
        _name = 'log.incident'
        _description = 'Incident / Task Resolution Log'

        # 1. Informacion general

        task_id = fields.Many2one('project.task', string="Tarea")
        project_name = fields.Char(string="Nombre del proyecto")
        module = fields.Char(string="Modulo o componente afectado")
        client = fields.Char(string="Cliente / area funcional")

        environment = fields.Selection([
                ('fw', 'Firmware'),
                ('sw', 'Software'),
                ('hw', 'Hardware'),
        ], string="Equipo")

        detection_date = fields.Date(string="Fecha de deteccion")
        resolution_date = fields.Date(string="Fecha de resolucion")
        responsible = fields.Char(string="Responsable principal")
        team = fields.Char(string="Equipo involucrado")

        # 2. Descripcion

        summary = fields.Char(string="Resumen breve")
        description = fields.Text(string="Descripcion detallada")

        impact = fields.Selection([
                ('blocker', 'Bloqueante'),
                ('high', 'Alto'),
                ('medium', 'Medio'),
                ('low', 'Bajo'),
        ])

        impact_description = fields.Text()

        # 3. Deteccion
        detection_method = fields.Selection([
                ('user', 'Usuario'),
                ('monitoring', 'Monitorizacion'),
                ('logs', 'Logs'),
                ('testing', 'Testing'),
                ('manual', 'Revision manual'),
                ('other', 'Otro')
        ])

        logs = fields.Text()
        screenshots = fields.Char()
        transaction_ids = fields.Char()
        stacktrace = fields.Text()

        # 4. Analisis tecnico

        root_cause = fields.Text()
        contributing_factors = fields.Text()
        systems = fields.Text()

        # 5. Resolucion

        action_taken = fields.Text()
        solution_description = fields.Text()
        modified_files = fields.Text()
        pr = fields.Char()
        commit = fields.Char()
        ticket = fields.Char()
        branch = fields.Char()

        # 6. Validacion

        tests_unit = fields.Boolean()
        tests_integration = fields.Boolean()
        manual_validation = fields.Boolean()
        qa_validation = fields.Boolean()
        prod_validation = fields.Boolean()
        peer_review = fields.Boolean()
        validation_result = fields.Text()


        # 7. Prevencion

        prevention = fields.Text()

        # 8. Lecciones

        lessons_learned = fields.Text()

        # 9. Knowledge base

        keywords = fields.Char()
        related_incidents = fields.Text()

        # 10. Estado

        state = fields.Selection([
                ('resolved', 'Resuelto'),
                ('temporary', 'Temporal'),
                ('pending', 'Pendiente'),
                ('followup', 'Seguimiento'),
        ], string="Estado")