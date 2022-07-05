from odoo import http
from odoo.http import request



class R3(http.Controller):

 # Sample Controller Created
    @http.route('/r3/model/', website=True, auth='public')
    def r3_model(self, **kw):
        records = request.env['r3.profile'].sudo().search([])
        return request.render("asher.records_layout2", {
         'records': records })
        
         # Sample Controller Created
    @http.route('/r3/des/', website=True, auth='public')
    def r3_des(self, **kw):
        records = request.env['r3.profile'].sudo().search([])
        return request.render("asher.records_layout3", {
         'records': records })
        

    # Sample Controller Created
    @http.route('/r3/records/', website=True, auth='public')
    def r3_records(self, **kw):
        
        records = request.env['r3.profile'].sudo().search([])
        return request.render("asher.records_layout", {
         'records': records })



    @http.route('/r3', type='json', auth='public')
    def get_r3(self, **kw):
        print("Yes here entered")
        r3_rec = request.env['r3.profile'].sudo().search([])
        records_r3 = []
        for rec in r3_rec:
            vals = {
                'product_name': rec.product_name,
                'product_model': rec.product_model,
                'product_description': rec.product_description,
            }
            records_r3.append(vals)
        print("Product List--->", records_r3)
        data = {'status': 200, 'response': records_r3, 'message': 'Done All R3 Records Returned'}
        return data