# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class revision_set(models.Model):
    _name = 'revisar_procesos_produccion.revision_set'
    _description = 'Conjunto de revisiones'
    _rec_name = 'code'

    code = fields.Char(size=10, string="Código", default=lambda self: self._generate_revision_set_code())
    state = fields.Selection([('0','Iniciada'),('1','En proceso'),('2','Terminada')],default = '0', required=True, string="Estado")
    date = fields.Date(string="Fecha")    
    description = fields.Text(string="Descripción")


    # Relación con revision
    revisions_ids = fields.One2many('revisar_procesos_produccion.revision','revision_set_id', string="Revisiones")

    # Generar código predeterminado
    @api.model
    def _generate_revision_set_code(self):
        year = str(datetime.date.today().year)
        last_revision_set = self.search([], order='id desc', limit=1)
        if last_revision_set:
            last_code = last_revision_set.code
            last_number = int(last_code[-2:])  # Obtenemos los últimos 2 carácteres del código.
            new_number = last_number + 1
            new_code = "CONJ" + year + str(new_number).zfill(2)  # Rellenar con ceros a la izquierda
        else:
            new_code = "CONJ" + year + "01"
        return new_code