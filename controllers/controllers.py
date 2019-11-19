# -*- coding: utf-8 -*-
from odoo import http

# class CustomePos(http.Controller):
#     @http.route('/customize-pos/customize-pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customize-pos/customize-pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custome_pos.listing', {
#             'root': '/customize-pos/customize-pos',
#             'objects': http.request.env['customize-pos.customize-pos'].search([]),
#         })

#     @http.route('/customize-pos/customize-pos/objects/<model("customize-pos.customize-pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customize-pos.object', {
#             'object': obj
#         })