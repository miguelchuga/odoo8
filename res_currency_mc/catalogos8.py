# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields
from openerp.tools import config
import datetime
import time
import sys

class marcas(osv.osv):
    _name = 'marcas'
    _description = 'Marcas'
    _rec_name = 'nombre'
    _columns = {
        'codigo': fields.char('Código', size=5, required=True),
        'nombre': fields.char('Marca', size=40, required=True),
    }
    _order = 'codigo'

class tipos_productos(osv.osv):
    _name = 'tipos_productos'
    _description = 'Tipos de Productos'
    _rec_name = 'nombre'
    _columns = {       
        'nombre': fields.char('Tipo Producto', size=40, required=True)
    }
    _order = 'nombre'

class lineas(osv.osv):
    _name = 'lineas'
    _description = 'Lineas'
    _rec_name = 'nombre'
    _columns = {       
        'nombre': fields.char('Línea', size=40, required=True)
    }
    _order = 'nombre'

class materiales(osv.osv):
    _name = 'materiales'
    _description = 'Materiales'
    _rec_name = 'nombre'
    _columns = {       
        'nombre': fields.char('Material', size=40, required=True),
        'abreviatura': fields.char('Abreviatura', size=10, required=True)
    }
    _order = 'nombre'

class componentes(osv.osv):
    _name = 'componentes'
    _description = 'Componentes'
    _rec_name = 'nombre'
    _columns = {
        'nombre': fields.char('Nombre', size=40, required=True),
        'abreviatura': fields.char('Abreviatura', size=5, required=True)
    }
    _order = 'nombre'

class caracteristicas(osv.osv):
    _name = 'caracteristicas'
    _description = 'Caracteristicas'
    _rec_name = 'nombre'
    _columns = {
        'nombre': fields.char('Característica', size=40, required=True)
    }
    _order = 'nombre'