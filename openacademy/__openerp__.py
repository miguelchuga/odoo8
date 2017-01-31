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
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Open Academy',
    'version': '0.1',
    'website' : 'https://www.odoo.com/page/events',
    'category': 'Training',
    'summary': 'This module is to intent........',
    'description': """
Open Academy
Training module
""",
    'author': 'Miguel',
    'depends': ['base','mail','report'],
    'data': ['openacademy_view.xml','partner_view.xml','openacademy_workflow.xml','security/groups.xml','security/ir.model.access.csv',
             'report/session.xml','openacademy_report.xml','openacademy_dashboard.xml','wizard/enroll_view.xml',
    ],
    'demo': [
        
    ],
    'test': [
    ],
    'installable': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
