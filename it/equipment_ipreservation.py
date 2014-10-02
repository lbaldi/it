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
from openerp.osv import fields, osv
from openerp import tools


class it_equipment_ipreservation(osv.osv):

    _name = 'it.equipment.ipreservation'

    _description = 'IP Reservation'

    _columns = {

        'name': fields.char('Name', required=True),
        'mac_address': fields.char('MAC Address', required=True),
        'ip_address': fields.char('IP Address', required=True),
        'equipment_id': fields.many2one('it.equipment','Equipment', ondelete='cascade'),

    }

it_equipment_ipreservation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
