# -*- coding: utf-8 -*-

from odoo import models, fields, api


class revision_verification(models.Model):
    _name = 'revisar_procesos_produccion.revision_verification'
    _description = 'Comprobaciones de una revisión'
    _rec_name = 'code'

    code = fields.Char(required=True, size=7, string="Código")
    description = fields.Text()
    state = fields.Selection([('0','Correcta'),('1','Incorrecta')], string="Estado")
    error = fields.Char()
    observation = fields.Text(string="Observaciones")


    # Relación con revision
    revision_id = fields.Many2one('revisar_procesos_produccion.revision', string="Revisión")
    revision_name = fields.Char(related='revision_id.name')
    verifications_ids = fields.One2many(related='revision_id.verifications_ids', string="Comprobaciones", readonly=True) # QUITAR??


    # Registro comprobaciones revisión:
    """ entrada = 1
    verifications = self.env['revisar_procesos_produccion.verification'].search([])
    for i in verifications:
        ns = self.env['revisar_procesos_produccion.revision_verification'].create({'code':entrada,'description':i.name}) """


