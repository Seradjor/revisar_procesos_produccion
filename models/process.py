# -*- coding: utf-8 -*-

from odoo import models, fields, api


class process(models.Model):
    _name = 'revisar_procesos_produccion.process'
    _description = 'Procesos de la línea de producción'
    _rec_name = 'name'

    code = fields.Char(size = 3, required=True, string="Código")
    name = fields.Char(required=True, string="Nombre proceso")
    description = fields.Text(string="Descripción del proceso") 


    # Relación con revision
    revisions_ids = fields.One2many('revisar_procesos_produccion.revision','process_id', string="Revisiones")

    # Relación con verification
    verifications_ids = fields.One2many('revisar_procesos_produccion.verification','process_id', string="Comprobaciones")
    