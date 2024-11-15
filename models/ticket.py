from odoo import models, fields, api

class TicketCategory(models.Model):
    _name = 'ticket.category'
    _description = 'Ticket Category'

    name = fields.Char(string='Category Name', required=True)


class TicketPriority(models.Model):
    _name = 'ticket.priority'
    _description = 'Ticket Priority'

    name = fields.Char(string='Priority Level', required=True)


class SupportTicket(models.Model):
    _name = 'support.ticket'
    _description = 'Support Ticket'

    name = fields.Char(string='Ticket Number', required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('support.ticket')) #, default=lambda self: self.env['ir.sequence'].next_by_code('support.ticket')
    category_id = fields.Many2one('ticket.category', string='Category')
    priority_id = fields.Many2one('ticket.priority', string='Priority')
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ], string='Status', default='open')
    user_id = fields.Many2one('res.users', string='Assigned To')
    
    # @api.model
    # def create(self, vals):
    #     if 'name' not in vals or vals['name'] == '/':
    #         vals['name'] = self.env['ir.sequence'].next_by_code('support.ticket')
    #     return super(SupportTicket, self).create(vals)
