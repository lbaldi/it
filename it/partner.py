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

import openerp
from openerp.osv import fields, osv

class res_partner(osv.osv):

    _name = "res.partner"

    _inherit= "res.partner"

    def _equipment_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict(map(lambda x: (x,0), ids))
        # The current user may not have access rights
        try:
            for partner in self.browse(cr, uid, ids, context):
                res[partner.id] = len(partner.equipment_ids)
        except:
            pass
        return res
        
    def _access_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict(map(lambda x: (x,0), ids))
        # The current user may not have access rights
        try:
            for partner in self.browse(cr, uid, ids, context):
                res[partner.id] = len(partner.access_ids)
        except:
            pass
        return res
        
    def _backup_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict(map(lambda x: (x,0), ids))
        # The current user may not have access rights
        try:
            for partner in self.browse(cr, uid, ids, context):
                res[partner.id] = len(partner.backup_ids)
        except:
            pass
        return res

    _columns = {

        'manage_it': fields.boolean('Manage IT'),
        'equipment_ids': fields.one2many('it.equipment', 'partner_id','Equipments'),
        'equipment_count': fields.function(_equipment_count, string="Equipments", type="integer"),
        'access_ids': fields.one2many('it.access', 'partner_id','Access'),
        'access_count': fields.function(_access_count, string="Access", type="integer"),
        'backup_ids': fields.one2many('it.backup', 'partner_id','Backups'),
        'backup_count': fields.function(_backup_count, string="Backups", type="integer"),

    }

res_partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
