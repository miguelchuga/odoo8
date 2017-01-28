from openerp.osv import osv, fields

class res_partner(osv.Model):
    
    _inherit='res.partner'
    _name='res.partner'
    
    _columns={'is_instructor':fields.boolean('Is Instructor'),
             'sessions_ids':fields.one2many('openacademy.session','instructor_id',string='Sessions')
             }
