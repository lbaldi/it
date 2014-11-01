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

import logging
import time
from openerp import tools, addons
from openerp.osv import fields, osv

_logger = logging.getLogger(__name__)

class it_equipment_configuration(osv.osv):

    _name = 'it.equipment.configuration'

    _description = 'Equipment Configuration'

    _order = 'date desc'

    _columns = {

        'name': fields.char('Description', size=64, required=True),
        'date': fields.datetime('Date'),
        'config_file': fields.binary('Configuration File', filename="config_file_filename"),
        'config_file_filename': fields.char('Configuration File Filename'),
        'equipment_id': fields.many2one('it.equipment','Equipment', ondelete='cascade'),

    }

    _defaults = {

        'date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),

    }

it_equipment_configuration()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
