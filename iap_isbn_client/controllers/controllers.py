# -*- coding: utf-8 -*-
# from odoo import http


# class IapIsbnClient(http.Controller):
#     @http.route('/iap_isbn_client/iap_isbn_client/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iap_isbn_client/iap_isbn_client/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iap_isbn_client.listing', {
#             'root': '/iap_isbn_client/iap_isbn_client',
#             'objects': http.request.env['iap_isbn_client.iap_isbn_client'].search([]),
#         })

#     @http.route('/iap_isbn_client/iap_isbn_client/objects/<model("iap_isbn_client.iap_isbn_client"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iap_isbn_client.object', {
#             'object': obj
#         })
