# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Leandro Ezequiel Baldi
#    <baldileandro@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

from openerp import addons
import logging
import time
from openerp.osv import fields, osv
from openerp import tools
_logger = logging.getLogger(__name__)

class it_application(osv.osv):

    _name = "it.application"

    _description = "Application"

    _columns = {

        'name': fields.char('Name', size=64, required=True),

        'company_id': fields.many2one('res.company', 'Company', required=True),
        'active': fields.boolean('Active'),
        'user_id': fields.many2one('res.users', 'Created by', readonly=True),
        'creation_date': fields.date('Creation Date',readonly=True),

        'developer': fields.char('Developer', size=64),
        'link_download': fields.char('Download Link', size=120),
        'link_page': fields.char('Link', size=120),
        'license_id': fields.many2one('it.application.license', 'License'),
        'type': fields.selection([('opensource','OPEN SOURCE'),('closedsource','CLOSED SOURCE')],'Type', required=True),
        'documentation': fields.binary('Documentation',filters='*', filename="documentation_filename"),
        'documentation_filename': fields.char('Documentation Filename'),
        'note': fields.text('Note'),

        'equipment_ids': fields.many2many('it.equipment','equipment_application_rel','application_id','equipment_id','Equipments'),

        # Closed Source
        'key': fields.char('Key', size=64),
        'keygen': fields.binary('Keygen',filters='*'),
        'crack': fields.binary('Crack',filters='*'),

    }

    _defaults = {

        'creation_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'active': True,
        'company_id': lambda self,cr,uid,ctx: self.pool['res.company']._company_default_get(cr,uid,object='it.equipment',context=ctx),
        'user_id': lambda self, cr, uid, ctx: uid,
        'type': 'opensource',

    }

it_application()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
