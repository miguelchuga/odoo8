from openerp.osv import osv, fields
    
class res_currency_rate(osv.Model):
    
    _inherit='res.currency.rate'
    
    _columns={'rate': fields.float('Rate', digits=(12, 10), help='The rate of the currency to the currency of rate 1'),
             }

res_currency_rate()

class res_currency(osv.Model):
    
    def _current_rate_silent(self, cr, uid, ids, name, arg, context=None):
        return self._get_current_rate(cr, uid, ids, raise_on_no_rate=False, context=context)
    
    _inherit='res.currency'
    
    _columns={'rate_silent': fields.function(_current_rate_silent, string='Current Rate', digits=(12,10),
                  help='The rate of the currency to the currency of rate 1 (0 if no rate defined).'),
             }

res_currency_rate()

