from openerp import models,fields,api,exceptions
from datetime import timedelta,date


class membresia_profesiones(models.Model):
    _name='membresia.profesiones'
    name=fields.Char('Name',required=True)
 
class membresia_privilegios(models.Model):
    _name='membresia.privilegios'
    _inherit=['mail.thread','ir.needaction_mixin']
    name=fields.Char('Name',required=True)
    description=fields.Text('Descriptions')

class membresia_historial_privilegios(models.Model):
    _name='membresia.historial_privilegios'
    miembro_id=fields.Many2one('res.partner',string='Miembro')
    fecha_inicio=fields.Date('Fecha Inicio',default=fields.Date.today)
    fecha_final =fields.Date('Fecha Final',default=fields.Date.today)
    privilegio_id=fields.Many2one('membresia.privilegios',string='Privilegio')
    description=fields.Text('Descripcion')
