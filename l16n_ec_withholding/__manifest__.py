# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Retenciones para Ecuador',
    'version': '16.0.1.0.0',
    'category': 'Generic Modules/Accounting',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'l10n_latam_invoice_document',
        'l16n_ec_partner'
    ],
    'author': 'danner.marante@citytech.ec',
    'website': '',
    'data': [
        'views/withholding_supplier_view.xml',
        'views/withholding_customer_view.xml',
        'security/ir.model.access.csv',
        # 'data/account.fiscal.position.csv',
        'views/account_invoice.xml',
        'views/el_company.xml',
        
        # 'views/report_account_move.xml',
         'views/report/reports.xml',
         'views/report/report_account_withdrawing.xml',
         
        
        # 'views/manual_retention.xml',
        # 'views/invoice_manual.xml',

    ]
}
