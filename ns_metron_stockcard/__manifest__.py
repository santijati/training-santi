{
    'name': "Nurosoft Metron Stock Card",
    'summary': "This module is for print stock card report",
    'description': "",
    'author': "Nurosoft - Santi Dev",
    'website': "http://www.nurosoft.id",
    'category': 'inventory',
    'version': '13.0.1.0',
    'depends': ['base', 'stock', ],
    'data': ['security/ir.model.access.csv',
             'views/ns_stock_card_menus.xml',
             'views/ns_stock_card_report.xml',
             'views/ns_stock_card_view.xml',
             ],
}
