from odoo import models, fields, api

class ropa_chula(models.Model):
    _name='ropa.chula'
    _description='Vestimenta'

    nombre=fields.Char('Nombre del producto',size=40, required=True,help='Nombre del producto')
    material=fields.Char('Material',size=30, required=True, help='Material con el que esta elaborado el producto')
    estampado=fields.Char('Estampado',size=50, required=False, help='Tematica del estampado')
    clasificacion=fields.Selection([
        ('H','Hombres'),
        ('M','Mujeres'),
        ('N','Niños')
    ], string='clasificacion')
    talla=fields.Integer()
    precio=fields.Integer()
    