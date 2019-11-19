# -*- coding: utf-8 -*-
from odoo import http

# class CustomePos(http.Controller):
#     @http.route('/custome_pos/custome_pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custome_pos/custome_pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custome_pos.listing', {
#             'root': '/custome_pos/custome_pos',
#             'objects': http.request.env['custome_pos.custome_pos'].search([]),
#         })

#     @http.route('/custome_pos/custome_pos/objects/<model("custome_pos.custome_pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custome_pos.object', {
#             'object': obj
#         })