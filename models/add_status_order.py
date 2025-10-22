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
        ],
        default='to_be_defined',
        string='Estado del presupuesto',
        tracking=True,
        help="Estado del pedido de venta para el seguimiento del proceso.",
        required=True
    )

    finished_date = fields.Datetime(
        string='Fecha de finalización',
        tracking=True,
        help="Fecha en la que el pedido de venta fue marcado como finalizado."
    )

    @api.onchange('status_order')
    def _onchange_status_order(self):
        if self.status_order == 'finished':
            self.finished_date = fields.Datetime.now()
            return

        if not self.finished_date or self.status_order == 'to_be_defined':
            self.finished_date = False
            return
