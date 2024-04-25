# -*- coding: utf-8 -*-

from odoo import models, fields, api


class error(models.Model):
    _name = 'revisar_procesos_produccion.error'
    _description = 'Errores encontrados en las comprobaciones de los procesos'
    _rec_name = 'code'

    code = fields.Char(size = 8, string="Código", default=lambda self: self._generate_error_number())
    name = fields.Char(required=True, string="Nombre")
    description = fields.Text(string="Descripción")


    # Relación con verification
    verifications_ids = fields.Many2many(
        comodel_name='revisar_procesos_produccion.verification', 
        relation='revisar_procesos_produccion_verification_error', 
        column1='error_id', 
        column2='verification_id', 
        string="Verificaciones")
    
    @api.model
    def _generate_error_number(self):
        last_error = self.search([], order='id desc', limit=1)
        if last_error:
            last_code = last_error.code
            last_number = int(last_code[5:])  # Excluyendo la longitud de "ERROR", obtenemos los últimos 3 dígitos del código.
            new_number = last_number + 1
            new_code = "ERROR" + str(new_number).zfill(3)  # Rellenar con ceros a la izquierda
        else:
            new_code = "ERROR" + '001'
        return new_code