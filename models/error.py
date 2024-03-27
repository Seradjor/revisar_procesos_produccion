# -*- coding: utf-8 -*-

from odoo import models, fields, api


class error(models.Model):
    _name = 'revisar_procesos_produccion.error'
    _description = 'Errores encontrados en las comprobaciones de los procesos'
    _rec_name = 'code'

    code = fields.Char(size = 5, required=True, string="Código")
    name = fields.Char(required=True, string="Nombre")
    description = fields.Text(string="Descripción")


    # Relación con verification
    verifications_ids = fields.Many2many(
        comodel_name='revisar_procesos_produccion.verification', 
        relation='revisar_procesos_produccion_verification_error', 
        column1='error_id', 
        column2='verification_id', 
        string="Verificaciones")