# -*- coding: utf-8 -*-
import odoo.addons.connector.backend as backend
import odoo.addons.magentoerpconnect.backend as magento_backend

magento_myversion = backend.Backend(parent=magento_backend.magento1700,
                                    version='1.7-myversion')
