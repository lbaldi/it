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

class it_equipment(osv.osv):

    _name = "it.equipment"

    _description = "Equipments"

    _rec_name = 'identification'

    def _get_identification(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = obj.name + " - " + obj.partner_id.name
        return result

    def name_search(self,cr,uid, name, args,context=None, limit=80, operator='ilike'):
        ids = []
        if name:
            ids = self.search(cr, uid,[('identification', operator, name)] + args,limit=limit, context=context)
        if not ids:
            ids = self.search(cr, uid,[('name', operator, name)] + args,limit=limit, context=context)
        return self.name_get(cr,uid,ids)

    _columns = {

        # For openerp structure
        'company_id': fields.many2one('res.company', 'Company', required=True),
        'active': fields.boolean('Active'),

        #General Info
        'identification': fields.function(_get_identification, type='char', string="Name", store=True),
        'name': fields.char('Name', size=64, required=True),
        'partner_id': fields.many2one('res.partner', 'Partner',required=True, domain="[('customer','=',1)]"),
        'function_ids': fields.many2many('it.equipment.function','equipment_function_rel','equipment_id','function_id','Functions'),
        'description': fields.char('Description', size=200, required=False),
        'note': fields.text('Note'),
        'image': fields.binary("Photo",help="Equipment Photo, limited to 1024x1024px."),
                        
        # Config Page
        'equipment_type': fields.selection([('physical','PHYSICAL'),('virtual','VIRTUAL'),('other','OTHER')],'Equipment Type',required=True),
        'is_contracted': fields.boolean('Contracted Service'),
        'is_dhcp': fields.boolean('DHCP'),
        'is_partitioned': fields.boolean('Partitions'),
        'is_backup': fields.boolean('Backup'),
        'is_access': fields.boolean('Access'),
        'is_os': fields.boolean('Operating System'),
        'function_dc': fields.boolean('Domain Controller'),
        'function_fileserver': fields.boolean('File Server'),

        'function_host': fields.boolean('Host'),
        'function_router': fields.boolean('Router'),

        # Audit Page
        'creation_date': fields.date('Creation Date',readonly=True),
        'user_id': fields.many2one('res.users', 'Created by',readonly=True),

        # Changes Page
        'change_ids': fields.one2many('it.equipment.change','equipment_id','Changes on this equipment'),

        # Contract Page
        'contract_partner_id': fields.many2one('res.partner', 'Contractor', domain="[('supplier','=',1)]"),
        'contract_client_number': fields.char('Client Nummber'),
        'contract_owner': fields.char('Titular'),
        'contract_nif': fields.char('NIF'),
        'contract_direction': fields.char('Invoice Direction'),

        # Virtual Machine Page
        'virtual_parent_id': fields.many2one('it.equipment', 'Equipment'),
        'virtual_memory_amount': fields.char('Memory'),
        'virtual_disk_amount': fields.char('Disk Size'),
        'virtual_processor_amount': fields.char('Number of Processor'),
        'virtual_network_amount': fields.char('Number of Network'),

        # Partition Page
        'partitions_ids': fields.one2many('it.equipment.partition','equipment_id','Partition on this equipment'),

        # Router Page
        'router_product': fields.many2one('product.product', 'Router'),
        'router_dhcp': fields.char('DHCP Range'),
        'router_dmz': fields.char('DMZ'),
        'router_forward_ids': fields.one2many('it.equipment.forward','equipment_id','Forward Rules'),
        'router_nat_ids': fields.one2many('it.equipment.nat','equipment_id','NAT Rules'),
        'router_rules_ids': fields.one2many('it.equipment.rule','equipment_id','Rules Registry'),

        # Network Configuration Page
        'equipment_network_ids': fields.one2many('it.equipment.network','equipment_id','Network on this equipment'),

        # Physical Page
        'physical_component_ids': fields.one2many('it.equipment.component','equipment_id','Components on this equipment'),

        # DC Page
        'dc_name': fields.char('Domain Name'),
        'dc_type': fields.selection([('primary','PRIMARY'),('secundary','SECUNDARY'),('slave','SLAVE')],'DC Type'),

        # Fileserver Page
        'equipment_mapping_ids': fields.one2many('it.equipment.mapping','equipment_id','Mappings'),

        # Fileserver Page
        'os_name': fields.char('OS Name'),
        'os_company': fields.char('OS Company'),
        'os_version': fields.char('OS Version'),

    }

    def _get_default_image(context=None):
        image_path = addons.get_module_resource('it', 'static/src/img/', 'default_image_equipment.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    _defaults = {
    
        'function_router': False,
        'function_host': False,
        'equipment_type': 'physical',
        'active': True,
        'is_dhcp': True,
        'is_partitioned': False,
        'is_backup': False,
        'is_access': True,
        'is_os': True,
        'function_dc': False,
        'function_fileserver': False,
        'image': _get_default_image(),
        'creation_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'user_id': lambda self, cr, uid, ctx: uid,
        'company_id': lambda self,cr,uid,ctx: self.pool['res.company']._company_default_get(cr,uid,object='it.equipment',context=ctx),
    
    }

it_equipment()
