# -*- encoding: utf-8 -*-

from openerp import models, fields, api, _


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def invoice_print(self):

        assert len(self) == 1, 'para imprimir solo 1 id al mismo tiempo'
        self.sent = True
#        return self.env['report'].get_action(self, 'forms_report.report_'+str(self.journal_id.paperformat_id.name)+'_form')
        return self.env['report'].get_action(self, self.journal_id.paperformat_id.name)
