# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddStatusOrder(models.Model):
    _inherit = 'sale.order'
    
    status_order = fields.Selection(
        [
            ('authorized', 'Autorizado'),
            ('processing', 'En proceso'),
            ('finished', 'Finalizado'),
        ], default='authorized', string='Estado del presupuesto', track_visibility='onchange', track_sequence=2,
        help="Estado del pedido de venta para el seguimiento del proceso."
    )