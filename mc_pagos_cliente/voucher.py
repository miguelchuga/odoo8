# -*- encoding: utf-8 -*-
from openerp import models,fields,api,exceptions
from datetime import timedelta,date

class account_voucher(models.Model):
    
    _inherit = 'account.voucher'

    fecha_recibo=fields.Date('Fecha Recibo ')
