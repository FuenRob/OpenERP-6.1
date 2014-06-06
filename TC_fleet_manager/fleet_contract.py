# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Top Consultant General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
##############################################################################

from osv import osv, fields

class fleet_contract(osv.osv):
    _name = 'fleet.contract'
    _columns = {
        'number': fields.char('number',size=20),
        'partner_id': fields.many2one('res.partner', 'Partner'),
        'vehicle_id': fields.many2one('fleet.vehicles', 'Vehicle'),
        'output_address': fields.char('Output Address',size=20),
        'address_route': fields.one2many('fleet.routes', 'address_route', 'Routes'),
    }
    
fleet_contract()

class fleet_routes(osv.osv):
    _name = 'fleet.routes'
    _columns = {
        'address_route': fields.char('Address Route',size=20),
        'priority': fields.char('Priority',size=20),
    }
    
fleet_routes()