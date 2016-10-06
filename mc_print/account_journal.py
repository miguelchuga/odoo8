# -*- encoding: utf-8 -*-
from openerp.osv import fields, osv


class account_journal(osv.osv):
    _inherit = 'account.journal'
 
    _columns={'paperformat_id': fields.many2one('report.paperformat', 'Paper format'),
              'lines_number': fields.integer('Lines number',help="Este valor controla la cantidad de lineas para imprimir los datos de pie de pagina del voucher"),
              'line_characters': fields.integer('Line characters'),
              'lines_voucher': fields.integer('Line voucher', help="Este valor controla la cantidad de lineas a imprimir en el voucher.."),
#              'lines_voucher_alternate': fields.integer('Line voucher alternate', help="Este valor controla la cantidad de lineas a imprimir en el voucher cuando no tiene en lines_voucher.."),

             }