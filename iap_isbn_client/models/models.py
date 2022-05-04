# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class iap_isbn_client(models.Model):
#     _name = 'iap_isbn_client.iap_isbn_client'
#     _description = 'iap_isbn_client.iap_isbn_client'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
