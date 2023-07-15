# -*- coding: utf-8 -*-
{
    'name' : 'Hospital Managment',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': 10,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['sale','mail'],
    'data': ['security/ir.model.access.csv', 'data/data.xml','views/patient.xml','views/kids.xml','views/sale.xml'],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
