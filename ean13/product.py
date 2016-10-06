# -*- encoding: utf-8 -*-
from openerp.osv import osv,fields
import openerp.addons.decimal_precision as dp


def check_ean_cod(eancode):
    print eancode

    return True


class product_product(osv.osv):

    _inherit = "product.product"


    def _check_ean_key(self, cr, uid, ids, context=None):
        for product in self.browse(cr, uid, ids, context=context):
            res = check_ean_cod(product.ean13)
        return res

    _constraints = [(_check_ean_key, 'Error: Invalid ean code', ['ean13'])]

product_product() 
