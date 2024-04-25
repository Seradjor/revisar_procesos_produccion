# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class revision(models.Model):
    _name = 'revisar_procesos_produccion.revision'
    _description = 'Revisión de un proceso'
    _rec_name = 'code'

    code = fields.Char(size=10, string="Código", default=lambda self: self._generate_revision_number())
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

    # Generar código predeterminado
    @api.model
    def _generate_revision_number(self):
        year = str(datetime.date.today().year)
        last_revision = self.search([], order='id desc', limit=1)
        if last_revision:
            last_code = last_revision.code
            last_number = int(last_code[7:])  # Excluyendo la longitud de "REV" y el año, obtenemos los últimos 3 dígitos del código.
            new_number = last_number + 1
            new_code = "REV" + year + str(new_number).zfill(3)  # Rellenar con ceros a la izquierda
        else:
            new_code = "REV" + year + "001"
        return new_code


    # Creación de comprobaciones de la revision, rescatando las comprobaciones de proceso a revisar.
    @api.onchange('process_id')
    def _process_change(self):
        if self.process_id:
            # Borrar verifications si ya hubiese seleccionado un proceso
            self.revision_verifications_ids.unlink()

            # Asignar el proceso seleccionado
            self.process_id = self.process_id

            # Buscar todos los registros de verificación asociados al mismo proceso
            verifications = self.env['revisar_procesos_produccion.verification'].search([('process_id.code', '=', self.process_id.code)])
            # Crear e imprimir la descripción de cada registro de verificación
            for verification in verifications:
                print("Descripción de verificación:", verification.description)
                self.env['revisar_procesos_produccion.revision_verification'].create({
                    'revision_id':self.id,
                    'code_revision':self.code,
                    'code':verification.code,
                    'description': verification.description
                })

            # Rellenar campo name
            self.name = f"Revisión proceso de {(self.process_name).lower()}"
        