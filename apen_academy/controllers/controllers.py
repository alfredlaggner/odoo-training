# -*- coding: utf-8 -*-
from odoo import http

# class ApenAcademy(http.Controller):
#     @http.route('/apen_academy/apen_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apen_academy/apen_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('apen_academy.listing', {
#             'root': '/apen_academy/apen_academy',
#             'objects': http.request.env['apen_academy.apen_academy'].search([]),
#         })

#     @http.route('/apen_academy/apen_academy/objects/<model("apen_academy.apen_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apen_academy.object', {
#             'object': obj
#         })