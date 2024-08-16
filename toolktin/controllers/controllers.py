# -*- coding: utf-8 -*-
# from odoo import http


# class Toolktin(http.Controller):
#     @http.route('/toolktin/toolktin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/toolktin/toolktin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('toolktin.listing', {
#             'root': '/toolktin/toolktin',
#             'objects': http.request.env['toolktin.toolktin'].search([]),
#         })

#     @http.route('/toolktin/toolktin/objects/<model("toolktin.toolktin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('toolktin.object', {
#             'object': obj
#         })

