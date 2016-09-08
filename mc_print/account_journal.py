# -*- encoding: utf-8 -*-
from openerp.osv import fields, osv


class account_journal(osv.osv):
    _inherit = 'account.journal'
 
    _columns={'paperformat_id': fields.many2one('report.paperformat', 'Paper format'),
              'lines_number': fields.integer('Lines number'),
              'line_characters': fields.integer('Line characters'),
             }