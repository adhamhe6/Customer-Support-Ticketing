from odoo import models, fields, api

class TicketCreationWizard(models.TransientModel):
    _name = 'ticket.creation.wizard'
    _description = 'Create Support Ticket'

    category_id = fields.Many2one('ticket.category', string='Category', required=True)
    priority_id = fields.Many2one('ticket.priority', string='Priority', required=True)
    description = fields.Text(string='Description', required=True)

    @api.model
    def create_ticket(self):
        ticket = self.env['support.ticket'].create({
            'category_id': self.category_id.id,
            'priority_id': self.priority_id.id,
            'description': self.description,
            'user_id': self.env.user.id,
        })

        # Notify the assigned user via email
        template = self.env.ref('customer_support_ticketing.email_template_new_ticket')
        if template:
            template.send_mail(ticket.id, force_send=True)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'support.ticket',
            'view_mode': 'form',
            'res_id': ticket.id,
            'target': 'current',
        }
