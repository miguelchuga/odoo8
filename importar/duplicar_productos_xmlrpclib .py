#- * -encoding: utf - 8 - * -

import xmlrpclib

username = 'admin' #the user
pwd = 'Mnbvcxz'      #the password of the user
dbname = 'o_fsrichard'    #the database

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://localhost:5069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://localhost:5069/xmlrpc/object')

args = [('company_id', '=',22 )] 
ids = sock.execute(dbname, uid, pwd, 'product.template', 'search', args)

fields = ['description','codigo_generado','genera_codigo','categ_id','ean13','type', 'list_price','name','default_code','cost_method','valuation','dolar_price','standard_price','default_code','description','currency_id'] 


for template in ids:

    args_id = [('id', '=',template )] 
    ids_t = sock.execute(dbname, uid, pwd, 'product.template', 'search', args_id)

    data = sock.execute(dbname, uid, pwd, 'product.template', 'read', ids_t, fields) 
    vals_template = {
       'type': 'product',
       'list_price':data[0]["list_price"],
       'name':data[0]["name"],
       'cost_method':'average',
       'valuation':'manual_periodic',
       'dolar_price':data[0]["dolar_price"],
       'currency_id':data[0]["currency_id"][0],
       'ean13':data[0]["ean13"],
       'standard_price':data[0]["standard_price"],
#       'categ_id':data[0]["categ_id"][0],
#       'taxes_id':67,
#       'supplier_taxes_id':65,
#       'property_account_income':  10860,
#       'property_account_expense':  1867,
       'genera_codigo':data[0]["genera_codigo"],
       'codigo_generado':data[0]["codigo_generado"],
       'description':data[0]["description"],
       'company_id':20,
       'description_purchase': data[0]["id"]

        }

    template_id = sock.execute(dbname, uid, pwd, 'product.template', 'create', vals_template)
    if template_id > 0:
         print "Valido : "+ str(template_id)
    else:
        print "ERROR:" + str(data[0]["id"])
    print vals_template




