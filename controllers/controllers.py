# -*- coding: utf-8 -*-
# from odoo import http


# class RevisarProcesosProduccion(http.Controller):
#     @http.route('/revisar_procesos_produccion/revisar_procesos_produccion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/revisar_procesos_produccion/revisar_procesos_produccion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('revisar_procesos_produccion.listing', {
#             'root': '/revisar_procesos_produccion/revisar_procesos_produccion',
#             'objects': http.request.env['revisar_procesos_produccion.revisar_procesos_produccion'].search([]),
#         })

#     @http.route('/revisar_procesos_produccion/revisar_procesos_produccion/objects/<model("revisar_procesos_produccion.revisar_procesos_produccion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('revisar_procesos_produccion.object', {
#             'object': obj
#         })
