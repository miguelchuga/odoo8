# -*- encoding: utf-8 -*-

#
# Este modulo tiene reportes personalizados para Guatemala.
    
#
# Status 1.0 - tested on Open ERP 5.0.6
#

{
    'name' : 'Números a Letras',
    'version' : '1.0',
    'category': 'Custom',
    'description': """Agrega la cantidad en letras a los cheques para su impresión""",
    'author': 'Miguel Chuga',
    'website': 'http://mcsistemas.net',
    'depends' : ['base','sale','account'],
    'init_xml' : [ ],
    'data': ["voucher_view.xml"],
    'demo_xml' : [ ],
    'update_xml' : [],
    'installable': True,
    'certificate': '',
}