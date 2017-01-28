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


    