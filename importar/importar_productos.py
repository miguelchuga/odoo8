#- * -encoding: utf - 8 - * -

import csv
import openerplib
import codecs

con = openerplib.get_connection(hostname = 'localhost', port = 8069, database = 'diste1', login = 'admin', password = 'Ytr3wqasdf')

con.check_login()

# Template
template_obj = con.get_model('product.template')


f = open('/home/cmike/src/trunk/odoo8/importar/productos.csv', 'rb')
reader = csv.reader(f, delimiter = ',')
index = 0
#21:36

# Lee cada registro.
for cadena in reader:

    if index > 0:

        try:

            #busca el ID de MARCA
            if len(cadena[1]) > 0:

            #INSERTA EN TEMPLATE
                vals_template = {
                    'type': 'product',
                    'list_price':cadena[3],
                    'name':cadena[1],
                    'default_code':cadena[0],
                    'cost_method':'average',
                    'standar_price':cadena[2],
                    'valuation':'real_time'
                }   
            template_id = template_obj.create(vals_template)

            print "===================="
            print cadena
            print "===================="

        except:
            print 'NO GRABO'
        pass

    index = index + 1
















for p in product_ids:
    producto = template_obj.search_read([('id', '=', p)])
    vals_template = {
       'type': 'product',
       'list_price':producto[0]["list_price"],
       'name':producto[0]["name"],
       'default_code':producto[0]["default_code"],
       'cost_method':producto[0]["cost_method"],
       'valuation':producto[0]["valuation"],
       'dolar_price':producto[0]["dolar_price"],
       'currency_id':producto[0]["currency_id"][0],
       'ean13':producto[0]["ean13"],
       'standard_price':producto[0]["standard_price"],
       'categ_id':producto[0]["categ_id"][0],
#       'taxes_id':  PONER EL ID DE IMPUESTOS DE CLIENTE
#       'supplier_taxes_id':  PONER EL ID DE IMPUESTOS DE PROVEEDOR
#       'property_account_income':  PONER EL ID de cuenta x cobrar DE CLIENTE    
#       'property_account_expense':  PONER EL ID de cuenta de gastos    
       'genera_codigo':producto[0]["genera_codigo"],
       'default_code':producto[0]["default_code"],
       'codigo_generado':producto[0]["codigo_generado"],
       'description':producto[0]["description"],
       'company_id':20,
    }   
    template_id = template_obj.create(vals_template)
    print "miguel"






