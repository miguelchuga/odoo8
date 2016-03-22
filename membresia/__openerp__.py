# -*- encoding: utf-8 -*-

#
# Personaliza partners para FS Richard.   
#
# Status 1.0 - tested on Odoo 8.0
#

{
    'name' : 'Membresia para Iglesias',
    'version' : '1.0',
    'category': 'Custom',
    'description': """Modulo especializado para control de membresias en una Iglesia""",
    'author': 'Miguel Chuga Martinez',
    'website': 'http://mcsistemas.net',
    'depends' : ['base','mail','sale','account'],
    'data': [ ],
    'init_xml' : [ ],
    'demo_xml' : [ ],
    'update_xml' : ['membresia_view.xml','partner_view.xml'],
    'installable': True,
    'certificate': '',
}
#,'catalogos_view.xml'
