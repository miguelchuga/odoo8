# -*- encoding: utf-8 -*-
from openerp.osv import osv, fields


class Partner(osv.Model):

    _inherit='res.partner'
    _name='res.partner'
    
    _columns = {
		'fecha_nacimiento': fields.date('Fecha Nacimiento', size=10),		
		'numero_id': fields.char('No. Identificación', size=20),
		'direccion_oficina': fields.char('Dirección Oficina', size=80),
		'telefono_oficina': fields.char('Teléfono de Oficina', size=20),
		'fax_oficina': fields.char('Fax de Oficina', size=20),
        'partner_conyuge_id': fields.many2one('res.partner', 'Conyuge', select=True),
        'profesiones_id': fields.many2one('membresia.profesiones', 'Profesión'),
        'estado_civil': fields.selection([('Soltero','Soltero'),('Casado','Casado'),('Divorciado','Divorciado'),('Unido','Unido'),('Otro','Otro')], 'Estado Civil'),

        'fecha_conversion'       : fields.date('Fecha de Conversion', size=10),        
        'lugar_conversion'       : fields.char('Lugar de Conversion', size=80),
        'donde_congregaba'       : fields.char('Donde se congraba',   size=80),
        'tiempo_asistir'         : fields.float('Tiempo de Asistir (Años/meses)',digits=(4,2) ),
        'todos_convertidos'      : fields.selection([('Si','Si'),('No','No')], 'Todos converticos ? '),
        'fecha_bautismo_agua'    : fields.date('Fecha de bautismo en agua', size=10),        
        'fecha_bautismo_es'      : fields.date('Fecha de bautismo en Espiritu Santo', size=10),        
        'carta_pastor'           : fields.selection([('Si','Si'),('No','No')], 'Se tralado con carta'),
        'asiste_discipulado'     : fields.selection([('Si','Si'),('No','No')], 'Asiste a un discipulado'),
        'se_indentifica'         : fields.selection([('Si','Si'),('No','No')], 'Se identifica con la doctrina de la Iglesia '),
        'doctrina_basica'        : fields.selection([('Si','Si'),('No','No')], 'Recibió doctrina basica'),
        'partner_discipulador_id': fields.many2one('res.partner', 'Discipulador', select=True),
        'partner_recomienda_id'  : fields.many2one('res.partner', 'Recomendado por', select=True),
        'observaciones'          : fields.text('Observaciones'),

            }

    