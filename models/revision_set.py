# -*- coding: utf-8 -*-

from odoo import models, fields, api


class revision_set(models.Model):
    _name = 'revisar_procesos_produccion.revision_set'
    _description = 'Conjunto de revisiones'
    _rec_name = 'code'

    code = fields.Char(required=True, size=9, string="Código")
    state = fields.Selection([('0','Iniciada'),('1','En proceso'),('2','Terminada')],default = '0', required=True, string="Estado")
    date = fields.Date(string="Fecha")    
    description = fields.Text(string="Descripción")


    # Relación con revision
    revisions_ids = fields.One2many('revisar_procesos_produccion.revision','revision_set_id', string="Revisiones")