import time
import util
from openerp.osv import osv
from openerp.report import report_sxw


class session_report_print(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        if context is None:
            context = {}
        super(session_report_print, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'percent': self._percent,
            'get_attendee':self._get_attendee,
            'util': util,
        })

#            'util': util,

    def _get_attendee(self,session_id):
        self.cr.execute("Select name from openacademy_attendee where session_id=%s"%session_id)
        return self.cr.fetchall()
                
    def _percent(self, d):
        return '%.2f%%'%(d*100)


class report_session(osv.AbstractModel):
    _name = 'report.openacademy.report_session'
    _inherit = 'report.abstract_report'
    _template = 'openacademy.report_session'
    _wrapped_report_class = session_report_print



