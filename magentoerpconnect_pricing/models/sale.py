# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2013 Camptocamp SA
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

from odoo.addons.magentoerpconnect.backend import magento
from odoo.addons.magentoerpconnect import sale
from odoo.addons.connector.unit.mapper import mapping


@magento(replacing=sale.SaleOrderImportMapper)
class SaleOrderImportMapper(sale.SaleOrderImportMapper):
    _model_name = 'magento.sale.order'

    @mapping
    def pricelist_id(self, record):
        """ Assign to the sale order the price list used on
        the Magento Website or Backend """
        website_binder = self.binder_for('magento.website')
        oe_website_id = website_binder.to_odoo(record['website_id'])
        website = self.session.browse('magento.website', oe_website_id)
        if website.pricelist_id:
            pricelist_id = website.pricelist_id.id
        else:
            pricelist_id = self.backend_record.pricelist_id.id
        return {'pricelist_id': pricelist_id}
