# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddStatusOrder(models.Model):
    _inherit = 'sale.order'
    
    status_order = fields.Selection(
        [
            ('to_be_defined', 'Por defninir'),
            ('authorized', 'Autorizado'),
            ('processing', 'En proceso'),
            ('finished', 'Finalizado'),
            ('invoiced', 'Facturado'),
        ], default='to_be_defined', string='Estado del presupuesto', track_visibility='onchange', track_sequence=2,
        help="Estado del pedido de venta para el seguimiento del proceso.", required=True
    )
    
    finished_date = fields.Datetime(string='Fecha de finalización', track_visibility='onchange', track_sequence=2)
    
    @api.onchange('status_order')
    def _onchange_status_order(self):
        if self.status_order == 'finished':
            self.finished_date = fields.Datetime.now()
        else:
            self.finished_date = False
            
            
            
            
            # Falta agregar lo de excel 