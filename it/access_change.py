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

class it_access_change(osv.osv):

    _name = "it.access.change"

    _description = "Access Change"

    _order = "creation_date desc"

    _columns = {

        'name': fields.char('Password', required=True, readonly=True),
        'access_id': fields.many2one('it.access', 'Access', required=True, ondelete='cascade'),
        'user_id': fields.many2one('res.users', 'Created by', readonly=True),
        'creation_date': fields.datetime('Creation Date',readonly=True),
        'note': fields.text('Note'),

    }

    _defaults = {

        'creation_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'user_id': lambda self, cr, uid, ctx: uid,

    }

it_access_change()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
