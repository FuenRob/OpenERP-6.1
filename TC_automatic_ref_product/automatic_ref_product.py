# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Top Consultant General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
##############################################################################

from osv import osv

class product_product(osv.osv):
    _inherit = 'product.product'

    def create(self, cr, uid, vals, context={}):
        """Sequence only assigned to product"""
        try:
            if (not vals['default_code'] or not vals['default_code'].strip()):
                vals['default_code'] = self.pool.get('ir.sequence').get(cr, uid, 'product.product')
        except KeyError:
            vals['default_code'] = self.pool.get('ir.sequence').get(cr, uid, 'product.product')
        return super(product_product, self).create(cr, uid, vals, context)

    def copy(self, cr, uid, ids, default=None, context=None):
        if not default:
            default = {}
        default.update({
            'default_code': '',                        
        })
        return super(product_product, self).copy(cr, uid, ids, default, context=context)

product_product()
