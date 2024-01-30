# -*- coding: utf-8 -*-
# from odoo import http


# class Modulo-hugo(http.Controller):
#     @http.route('/modulo-hugo/modulo-hugo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo-hugo/modulo-hugo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo-hugo.listing', {
#             'root': '/modulo-hugo/modulo-hugo',
#             'objects': http.request.env['modulo-hugo.modulo-hugo'].search([]),
#         })

#     @http.route('/modulo-hugo/modulo-hugo/objects/<model("modulo-hugo.modulo-hugo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo-hugo.object', {
#             'object': obj
#         })
