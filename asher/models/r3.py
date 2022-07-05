from odoo import fields, models


class r3Profile(models.Model):
    _name = "r3.profile"

    product_name = fields.Char(String="R3 Name", required = True)
    product_model = fields.Char(String="Model")
    product_description = fields.Text(String="Model")
    product_image1= fields.Binary(String="Image")
    product_image2= fields.Binary(String="Image")
    product_image3= fields.Binary(String="Image")