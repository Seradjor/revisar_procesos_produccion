# -*- coding: utf-8 -*-

from odoo import models, fields, api


class verification(models.Model):
    _name = 'revisar_procesos_produccion.verification'
    _description = 'Comprobaciones del proceso'
    _rec_name = 'code'

    code = fields.Char(size = 3, required=True, string="Código")
    name = fields.Char(required=True, string="Nombre")
    description = fields.Text(string="Descripción")


    # Relación con proceso
    process_id = fields.Many2one('revisar_procesos_produccion.process', string="Proceso")
    process_name = fields.Char(related='process_id.name')