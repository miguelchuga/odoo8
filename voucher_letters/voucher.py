# -*- encoding: utf-8 -*-
from openerp import models,fields,api,exceptions
from datetime import timedelta,date
#import util

class account_voucher(models.Model):

#    @api.one
#    def _calcular_letras(self):
#        self.valor_letras =  util.num_a_letras(self.amount)
    
    _inherit = 'account.voucher'
#    valor_letras=fields.Char("Letras",compute=_calcular_letras)
    hecho_por=fields.Char('Hecho por ',size=10)
    revisado_por=fields.Char('Revisado por ',size=10)
    autorizado_por=fields.Char('Autorizado por ',size=10)
    no_negociable=fields.Char('NO Negociable ',size=15,default='NO NEGOCIABLE')
    concepto_a=fields.Char('Concepto A ',size=85,default=' ')
    concepto_b=fields.Char('Concepto B ',size=85,default=' ')
    concepto_c=fields.Char('Concepto C ',size=85,default=' ')
