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

class fleet_vehicles(osv.osv):
    _name = 'fleet.vehicles'
    _columns = {
        'name': fields.char('Vehicle',size=20,required=True),
        'model': fields.char('model',size=20,required=True),
        'class': fields.char('class',size=20),
        'fuel': fields.selection([
                ('diesel','Diesel'),
                ('gasoline','Gasoline'),
                ],'Fuel',required=True),
        'employee_ids': fields.many2one('hr.employee', 'Employees'),
        'adquisition_date': fields.date('Adquisition Date',size=20),
        'cost': fields.char('Cost',size=20),
        'doors_number': fields.integer('Doors Number')
    }
    
fleet_vehicles()