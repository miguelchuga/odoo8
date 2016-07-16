# -*- encoding: utf-8 -*-
from openerp import models,fields,api,exceptions
from datetime import timedelta,date
import util

class account_voucher(models.Model):

    @api.one
    def _calcular_letras(self):
        self.valor_letras =  util.num_a_letras(self.amount)
    
    _inherit = 'account.voucher'
    valor_letras=fields.Char("Letras",compute=_calcular_letras)