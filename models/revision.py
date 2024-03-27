# -*- coding: utf-8 -*-

from odoo import models, fields, api


class revision(models.Model):
    _name = 'revisar_procesos_produccion.revision'
    _description = 'Revisión de un proceso'
    _rec_name = 'code'

    code = fields.Char(required=True, size=5, string="Código")
    name = fields.Char(required=True, string="Nombre")
    responsable = fields.Char()
    estado = fields.Selection([('0','Iniciada'),('1','En proceso'),('2','Terminada')],default = '0', required=True)
    fecha = fields.Date(string="Fecha revisión")

    process_id = fields.Many2one('revisar_procesos_produccion.process')
    process_name = fields.Char(related='process_id.name')
