# -*- encoding: utf-8 -*-

#
# Este modulo tiene reportes personalizados para Guatemala.
    
#
# Status 1.0 - tested on Open ERP 5.0.6
#

{
    'name' : 'Numeros a Letras',
    'version' : '1.0',
    'category': 'Custom',
    'description': """Agrega la cantidad en letras a las facturas para la impresion de las mismas""",
    'author': 'Miguel Chuga',
    'website': 'http://mcsistemas.net',
    'depends' : ['base','sale','account'],
    'init_xml' : [ ],
    'demo_xml' : [ ],
    'update_xml' : ["invoice_view.xml"],
    'installable': False,
    'certificate': '',
}
#,'catalogos_view.xml'
