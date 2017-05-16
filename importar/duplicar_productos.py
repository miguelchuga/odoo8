#- * -encoding: utf - 8 - * -

import openerplib
import codecs

con = openerplib.get_connection(hostname = 'localhost', port = 5069, database = 'o_fsrichard', login = 'admin', password = 'Mnbvcxz')

con.check_login()

# Template
template_obj = con.get_model('product.template')


#22 = la empresa ARS
#product_ids = template_obj.search([('company_id', '=',22),('type', '=', 'product')])

producto = template_obj.search_read([('id', '=', 43257)])

vals_template = {
#       'type': 'product',
       'list_price':producto[0]["list_price"],
       'name':producto[0]["name"],
       'default_code':producto[0]["default_code"],
       'cost_method':producto[0]["cost_method"],
       'valuation':producto[0]["valuation"],
       'dolar_price':producto[0]["dolar_price"],
#       'currency_id':producto[0]["currency_id"][0],
#       'ean13':producto[0]["ean13"],
       'standard_price':producto[0]["standard_price"],
#       'categ_id':producto[0]["categ_id"][0],
#       'taxes_id':  PONER EL ID DE IMPUESTOS DE CLIENTE
#       'supplier_taxes_id':  PONER EL ID DE IMPUESTOS DE PROVEEDOR
#       'property_account_income':  PONER EL ID de cuenta x cobrar DE CLIENTE    
#       'property_account_expense':  PONER EL ID de cuenta de gastos    
#       'genera_codigo':producto[0]["genera_codigo"],
       'default_code':producto[0]["default_code"],
#       'codigo_generado':producto[0]["codigo_generado"],
       'description':producto[0]["description"],
 #      'company_id':20
    }
template_id = template_obj.create(vals_template)
print "miguel"





