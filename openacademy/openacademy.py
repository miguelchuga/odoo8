from openerp import models,fields,api,exceptions
from datetime import timedelta,date


class openacademy_course(models.Model):
    _name='openacademy.course'
    name=fields.Char('Name',required=True)
    description=fields.Text('Descriptions')
    session_ids=fields.One2many('openacademy.session','course_id',string='Sessions')
    responsible_id=fields.Many2one('res.users',string='Responsible')
    _sql_constraints = [
        ('checknamedescription',
         'CHECK(name != description)',
         "The title of the course should not be the description"),
        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
    
    @api.one
    def copy(self,defaults):
        raise exceptions.ValidationError("no puede copiar")
#        defaults['name']='%s COPY'%self.name
#        return super(openacademy_course,self).copy(defaults)


class openacademy_session(models.Model):
    @api.one
    @api.depends('seats','attendee_ids')
    def _remaining_seats(self):
        self.remaining_seats= self.seats and (1.00-(float(len(self.attendee_ids))/self.seats))*100 or 0.0

    @api.multi
    @api.depends('attendee_ids.session_id','attendee_ids')
    def _attendee_count(self):
        for session in self:    
            session.attendee_count=len(session.attendee_ids) 
    
    @api.one
    @api.depends('duration','start_date')
    def _end_date(self):
        t=timedelta(days=self.duration-1)
        start=self.start_date.split('-')       
        self.end_date=date(int(start[0]),int(start[1]),int(start[2]))+t

    @api.one
    @api.depends('duration','start_date')
    def _end_date_inv(self):
        start=self.start_date.split('-')
        end=self.end_date.split('-')
        t=date(int(end[0]),int(end[1]),int(end[2]))-date(int(start[0]),int(start[1]),int(start[2]))
        self.duration=t.days+1

    @api.onchange('seats')
    def _seats(self):
        if self.seats < 0:
            return {'warning':{'title':'Data error',
                               'message':'The seats must be greater than zero...'
                               }
                    }    
    @api.one
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_in(self):
        for attendee in self.attendee_ids:
            if self.instructor_id == attendee.partner_id:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")

    _name='openacademy.session'
    _inherit=['mail.thread','ir.needaction_mixin']
    name=fields.Char('Name',required=True)
    start_date=fields.Date('Start Date',default=fields.Date.today)
    seats=fields.Integer('Seats')
    duration=fields.Float('Duration')
    course_id=fields.Many2one('openacademy.course',strin='Course')
    attendee_ids=fields.One2many('openacademy.attendee','session_id',string='Attendee')
    instructor_id=fields.Many2one('res.partner',string='Instructor')
#                                  domain=['|',('is_instructor','=',True),('category_id.name','in',['uno','dos'])])
    remaining_seats=fields.Float('Remain Seats',compute=_remaining_seats)
    attendee_count=fields.Integer("Attendee Count",compute=_attendee_count, store=True)
    end_date=fields.Date('End Date', compute=_end_date, inverse=_end_date_inv)
    active=fields.Boolean('active',default=True)
    color=fields.Integer('Color')
    state=fields.Selection([('draft','Draft'),
                            ('confirmed','Confirmed'),
                            ('done','Done')],string='State',readonly=True)

    @api.one
    def action_draft(self):
        self.state='draft'

    @api.one
    def action_confirmed(self):
        self.state='confirmed'

    @api.one
    def action_done(self):
        self.state='done'

class openacademy_attendee(models.Model):
    _name='openacademy.attendee'
    name=fields.Char('Name',required=True)
    session_id=fields.Many2one('openacademy.session',string='Session')
    partner_id=fields.Many2one('res.partner',string='Partner')
    _sql_constraints = [
        ('attendee_name_unique',
         'UNIQUE(session_id,partner_id)',
         "The Attendee must be unique"),
    ]
    
    
    
    