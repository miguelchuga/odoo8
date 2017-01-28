from openerp import models,fields,api

class openacademy_enroll(models.TransientModel):

    
    @api.model
    def _session_default(self):
        return self.env.context.get('active_id',False)
        
        
        
    _name='openacademy.enroll'
    session_id=fields.Many2one('openacademy.session',string='Session',default=_session_default)
    attendee_ids=fields.One2many('openacademy.enroll.attendee','enroll_id',string='Attendee')

    @api.one
    def action_enroll(self):

        session_ids=self.env.context.get('active_ids',[])
        if len(session_ids)<=1:
            session_ids=[self.session_id.id]

        for session_id in session_ids:
            for attendee in self.attendee_ids:
                self.env['openacademy.attendee'].create({'name':attendee.name,
                                                         'partner_id':attendee.partner_id.id,
                                                         'session_id':session_id})


class openacademy_enroll_attendee(models.TransientModel):
    _name='openacademy.enroll.attendee'
    name=fields.Char('Name',required=True)
    enroll_id=fields.Many2one('openacademy.enroll',string='Enroll')
    partner_id=fields.Many2one('res.partner','Partner')
