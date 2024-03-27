# -*- coding: utf-8 -*-

from odoo import models, fields, api


class revision_verification(models.Model):
    _name = 'revisar_procesos_produccion.revision_verification'
    _description = 'Comprobaciones de una revisión'
    _rec_name = 'code'

    code = fields.Char(required=True, size=7, string="Código")
    state = fields.Selection([('0','Correcta'),('1','Incorrecta')], required=True, string="Estado")
    error = fields.Char()
    observation = fields.Text(string="Observaciones")


    # Relación con revision
    revision_id = fields.Many2one('revisar_procesos_produccion.revision', string="Revisión")
    revision_name = fields.Char(related='revision_id.name')