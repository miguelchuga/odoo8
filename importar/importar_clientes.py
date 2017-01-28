#!/usr/bin/python
# -*- encoding: utf-8 -*-

import csv
import openerplib
import codecs


con = openerplib.get_connection(hostname='localhost',port=8069,database='diste9',login='admin',password='Ytr3wqasdf')

con.check_login()

# Crea instancia de clientes.
clientes_obj=con.get_model('res.partner')

f = open('/home/cmike/src/trunk/odoo8/importar/clientes2.csv','rb')
reader = csv.reader(f,delimiter=',')
index = 1

# Lee cada registro.
for cadena in reader:

	if index > 0:
	
		try:

			vals_partner = {
				'is_customer': 1,
				'name': cadena[8],
				'street': cadena[6],
				'ref': cadena[5],
				'city': cadena[7],
			}

			clientes_obj.create(vals_partner)

		except:
			print 'Registro con problemas, no fue grabado '+cadena[0]
			print 'Registro no grabado!!!'
			pass

	index = index + 1
