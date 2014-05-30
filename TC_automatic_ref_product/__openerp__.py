# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Roberto Morais.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Top Consultant General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
##############################################################################

{
    "name" : "Automatic Ref Product",
    "version": "1.1",
    "author" : "Top Consultant",
    "website" : "http://www.topconsultant.es/",
    "category": 'Product',
    "depends" : ["base", "product"],
    "description": """
Automatic Reference Product
============================

This module is responsible for allocating a reference to all product.
    """,
    "init_xml" : [],
    "update_xml": ['automatic_ref_product.xml'],
    'demo_xml': [
    ],
    'installable': True,
    'auto_install': False,
    'certificate' : "",
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
