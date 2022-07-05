from odoo import http
from odoo.http import request



class Test(http.Controller):

    # Sample Controller Created
    @http.route('/test', website=True, auth='public')
    def r3_records(self, **kw):
        
        #records = request.env['r3.profile'].sudo().search([])
        return request.render("asher.test_layout", {})
