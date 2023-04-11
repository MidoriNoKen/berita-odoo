# -*- coding: utf-8 -*-
# from odoo import http


# class Berita(http.Controller):
#     @http.route('/berita/berita', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/berita/berita/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('berita.listing', {
#             'root': '/berita/berita',
#             'objects': http.request.env['berita.berita'].search([]),
#         })

#     @http.route('/berita/berita/objects/<model("berita.berita"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('berita.object', {
#             'object': obj
#         })
