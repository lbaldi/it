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

class it_backup(osv.osv):

    _name = "it.backup"

    _description = "Back Up"

    _columns = {

        'equipment_id': fields.many2one('it.equipment', 'Equipment', domain="[('is_backup','=',1)]", ondelete='cascade',required=True),
        'partner_id': fields.related('equipment_id','partner_id',readonly=True, type='many2one',relation='res.partner', string='Partner',store=True),
        'name': fields.char('Name',required=True),
        'type': fields.selection([('diff','DIFF'),('full','FULL'),('inc','INCREMENTAL'),('other','OTHER')],'Backup Type',required=True),
        'destination': fields.char('Destination'),
        'source': fields.char('Source'),
        'script': fields.binary('Script',filters='*', filename="script_filename"),
        'script_filename': fields.char('Script Filename'),
        'script_location': fields.char('Script Location'),
        'frequency': fields.char('Frequency'),
        'time_schedule': fields.float('Time Schedule'),
        'note': fields.text('Note'),
        'company_id': fields.many2one('res.company', 'Company', required=True),
        'user_id': fields.many2one('res.users', 'Created by', readonly=True),
        'creation_date': fields.date('Creation Date',readonly=True),
        'active': fields.boolean('Active'),

    }

    _defaults = {

        'type': 'full',
        'creation_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'active': True,
        'company_id': lambda self,cr,uid,ctx: self.pool['res.company']._company_default_get(cr,uid,object='it.equipment',context=ctx),
        'user_id': lambda self, cr, uid, ctx: uid,

    }

it_backup()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
