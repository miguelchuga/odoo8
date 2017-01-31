# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#'report/invoice.xml',
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# diazreyes
##############################################################################

{
    'name': 'Extiende la funcionalidad para formas Pre-impresas',
    'version': '0.1',
    'website': 'https://mcsistemas.net',
    'category': 'Reports/pdf',
    'author': 'Miguel Chuga',
    'depends': ['base','account'],
    'data': ['view/account_journal_view.xml',
             'view/account_voucher_view.xml',
             'view/account_invoice_view.xml',
    ],
    'demo': [
        
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'css': ['static/css/forms_report.css'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
