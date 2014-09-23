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

class it_equipment_rule(osv.osv):

    _name = 'it.equipment.rule'

    _description = 'Equipment Rules'

    _columns = {

        'equipment_id': fields.many2one('it.equipment','Equipment', ondelete='cascade'),
        'name': fields.char('Name', required=True),
        'source_port': fields.char('Source Port'),
        'destination_port': fields.char('Destination Port'),
        'source_address': fields.char('Source Address'),
        'destination_address': fields.char('Destination Address'),
        'permission': fields.selection([('allow','ALLOW'),('deny','DENY')],'Permission'),

    }

    _defaults = {

        'permission': 'allow',

    }

it_equipment_rule()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
