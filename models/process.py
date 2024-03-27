# -*- coding: utf-8 -*-

from odoo import models, fields, api


class process(models.Model):
    _name = 'revisar_procesos_produccion.process'
    _description = 'Procesos de la línea de producción'
    _rec_name = 'code'

    code = fields.Char(size = 3, required=True, string="Código")
    name = fields.Char(required=True, string="Nombre proceso")
    description = fields.Text(string="Descripción del proceso")

    revisions_ids = fields.One2many('revisar_procesos_produccion.revision','process_id')