# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2013 Camptocamp SA
#    Copyright 2013 Akretion
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

{'name': 'Magento Connector',
 'version': '10.0.1.0.0',
 'category': 'Connector',
 'depends': ['account',
             'product',
             'delivery',
             'sale_stock',
             'connector_ecommerce',
             'product_multi_category',
             ],
 'external_dependencies': {
     'python': ['magento'],
 },
 'author': "Camptocamp,Akretion,Odoo Community Association (OCA)",
 'license': 'AGPL-3',
 'website': 'http://www.odoo-magento-connector.com',
 'images': ['images/magento_backend.png',
            'images/jobs.png',
            'images/product_binding.png',
            'images/invoice_binding.png',
            'images/magentoerpconnect.png',
            ],
 'demo': [],
 'data': ['security/ir.model.access.csv',
          'data/magentoerpconnect_data.xml',
          'views/magentoerpconnect_menu.xml',
          'views/setting_view.xml',
          'views/magento_model_view.xml',
          'views/product_view.xml',
          'views/partner_view.xml',
          'views/sale_view.xml',
          'views/invoice_view.xml',
          'views/delivery_view.xml',
          'views/stock_view.xml',
          'views/account_payment_mode_view.xml',
          ],
 'installable': True,
 'application': True,
 }
