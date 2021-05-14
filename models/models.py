from odoo import models, fields, api, exceptions

class practicas_student(models.Model):
    _name = "practicas.student"
    _description = "Modelo para formulario de estudiantes"
    name = fields.Char('Nombre', size = 128)
    last_name = fields.Char('Apellido', size = 128)
