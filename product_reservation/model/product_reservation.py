from odoo import models, fields, api


class ProductReservation(models.Model):
    _name = "product_reservation"
    _description = "reservation"
    sequence = fields.Char('Order Reference', required=True, index=True,
                           copy=False, default='NEW')
    name = fields.Char(required=True)
    customer_id = fields.Many2one('res.partner', string='Select Customer')
    expiry_date = fields.Date()
    internal_note = fields.Html(placeholder="Internal note")
    multi_product = fields.Many2many('product.product',
                                     string='select products', required=True)

    @api.model
    def create(self, vals):
        if vals.get('sequence', 'NEW') == 'NEW':
            vals['sequence'] = self.env['ir.sequence'].next_by_code(
                'product.reservation') or 'NEW'
        result = super(ProductReservation, self).create(vals)
        return result
