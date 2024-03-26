# -*- coding: utf-8 -*-

from odoo import models, fields, api


class proceso(models.Model):
    _name = 'revisar_procesos_produccion.proceso'
    _description = 'Procesos de la línea de producción'
    _rec_name = 'id_process'

    id_process = fields.Char()
    name = fields.Char()
    process_description = fields.Text()
