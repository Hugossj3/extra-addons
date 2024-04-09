from odoo import models, fields, api

class videoclub_pelis(models.Model):
    _name='videoclub.pelis'
    _description='Peliculas'

    titulo=fields.Char('Titulo',size=30, required=True,help='Nombre de la peli')
    director=fields.Char('Director',size=30,required=False, help='Director de la peli', default='')
    clasificacion=fields.Selection([
        ('TP','Todos los publicos'),
        ('men12','Menores de 12'),
        ('may18','Mayores 18')
    ], string='clasificacion', default='TP')
    presupuesto=fields.Integer()
    fechaestreno=fields.Date()
    subvencionado=fields.Integer(compute='_valor_subvencion')
    invertido=fields.Integer(compute='_valor_inversion')

@api.depends('presupuesto')
def _valor_subvencion(self):
    for record in self:
        record.subvencionado = record.presupuesto * 0.3

@api.depends('presupuesto')
def _valor_inversion(self):
    for record in self:
        record.invertido = record.presupuesto * 0.7


