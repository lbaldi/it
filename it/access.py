# -*- encoding: utf-8 -*-
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

class it_access(osv.osv):

    _name = "it.access"

    _description = "Access"

    _columns = {
    
		'name': fields.char('Name', size=64, required=True),
		'company_id': fields.many2one('res.company', 'Company', required=True),
		'equipment_id': fields.many2one('it.equipment', 'Equipment', ondelete='cascade',required=True),
		'user_id': fields.many2one('res.users', 'Created by', readonly=True),
		'application': fields.char('Application', size=64),
		'user': fields.char('User', size=64),
		'password': fields.char('Password', size=64),
		'port': fields.char('Port'),
		'partner_id': fields.related('equipment_id','partner_id',readonly=True, type='many2one',relation='res.partner', string='Partner',store=True),
		'description': fields.char('Description', size=120),
		'link': fields.char('Link', size=120),
		'creation_date': fields.date('Creation Date',readonly=True),
		'active': fields.boolean('Active'),
		'ssl_csr': fields.binary('CSR',filters='*.csr'),
		'ssl_cert': fields.binary('Cert',filters='*'),
		'ssl_publickey': fields.binary('Public Key',filters='*'),
		'ssl_privatekey': fields.binary('Private Key',filters='*'),
		'note': fields.text('Note'),
		
    }

    _defaults = {
    
		'creation_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
		'active': True,
		'company_id': lambda self,cr,uid,ctx: self.pool['res.company']._company_default_get(cr,uid,object='it.equipment',context=ctx),
		'user_id': lambda self, cr, uid, ctx: uid,
    
    }

it_access()
