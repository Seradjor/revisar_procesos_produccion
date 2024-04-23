# -*- coding: utf-8 -*-

from odoo import models, fields, api


class revision(models.Model):
    _name = 'revisar_procesos_produccion.revision'
    _description = 'Revisión de un proceso'
    _rec_name = 'code'

    code = fields.Char(required=True, size=8, string="Código")
    name = fields.Char(required=True, string="Nombre")
    responsable = fields.Char()
    state = fields.Selection([('0','Iniciada'),('1','En proceso'),('2','Terminada')],default = '0', required=True, string="Estado")
    date = fields.Date(string="Fecha revisión")


    # Relación con process
    process_id = fields.Many2one('revisar_procesos_produccion.process', string="Proceso")
    process_name = fields.Char(related='process_id.name')
    verifications_ids = fields.One2many(related='process_id.verifications_ids', string="Comprobaciones", readonly=True) # QUITAR??

    # Relación con revision_verification
    revision_verifications_ids = fields.One2many('revisar_procesos_produccion.revision_verification','revision_id', string=" ")
    revision_verification_name = fields.Text(related='revision_verifications_ids.description', string="Comprobación revisión")

    # Relación con revision_set
    revision_set_id = fields.Many2one('revisar_procesos_produccion.revision_set')
    revision_set_code = fields.Char(related='revision_set_id.code')
    
    # Creación de comprobaciones de la revision, rescatando las comprobaciones de proceso a revisar.
    @api.onchange('process_id')
    def _on_state_change(self):
        # Buscar todos los registros de verificación asociados al mismo proceso
        verifications = self.env['revisar_procesos_produccion.verification'].search([('process_id.code', '=', self.process_id.code)])
        # Imprimir la descripción de cada registro de verificación
        for verification in verifications:
            print("Descripción de verificación:", verification.description)
            self.env['revisar_procesos_produccion.revision_verification'].create({
                'revision_id': self.id,
                'description': verification.description
            })