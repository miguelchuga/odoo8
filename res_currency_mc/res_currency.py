from openerp.osv import osv, fields
    
class res_currency_rate(osv.Model):
    
    _inherit='res.currency.rate'
    
    _columns={'rate': fields.float('Rate', digits=(12, 10), help='The rate of the currency to the currency of rate 1'),
             }

res_currency_rate()

class res_currency(osv.Model):
    
    _inherit='res.currency'
    
    _columns={'rate': fields.float('Rate', digits=(12, 10), help='The rate of the currency to the currency of rate 1'),
             }

res_currency_rate()

