# -*- coding: utf-8 -*-

from odoo import models, fields, api


class revision(models.Model):
    _name = 'revisar_procesos_produccion.revision'
    _description = 'Revisión de un proceso'
    _rec_name = 'code'

    code = fields.Char(required=True, size=5, string="Código")
    name = fields.Char(required=True, string="Nombre")
    responsable = fields.Char()
    state = fields.Selection([('0','Iniciada'),('1','En proceso'),('2','Terminada')],default = '0', required=True, string="Estado")
    date = fields.Date(string="Fecha revisión")


    # Relación con process
    process_id = fields.Many2one('revisar_procesos_produccion.process', string="Proceso")
    process_name = fields.Char(related='process_id.name')

    # Relación con revision_verification
    revision_verifications_ids = fields.One2many('revisar_procesos_produccion.revision_verification','revision_id', string="Comprobaciones")

    # Relación con revision_set
    revision_set_id = fields.Many2one('revisar_procesos_produccion.revision_set')
    revision_set_code = fields.Char(related='revision_set_id.code')
