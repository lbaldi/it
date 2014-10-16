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
import random
from random import choice
from openerp.osv import fields, osv
from openerp import tools
_logger = logging.getLogger(__name__)

class it_equipment(osv.osv):

    _name = "it.equipment"

    _description = "Equipments"

    _rec_name = 'identification'

    def _get_pin(self, cr, uid, context=None):
        context = context or {}
        longitud = 12
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        return p

    def _get_identification(self, cr, uid, ids, name, args, context=None):
        context = context or {}
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = obj.name + " - " + obj.partner_id.name
        return result

    def name_search(self, cr, uid, name, args, context=None, limit=80, operator='ilike'):
        context = context or {}
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
        'name': fields.char('Name', required=True),
        'partner_id': fields.many2one('res.partner', 'Partner',required=True, domain="[('manage_it','=',1)]"),
        'function_ids': fields.many2many('it.equipment.function','equipment_function_rel','equipment_id','function_id','Functions'),
        'description': fields.char('Description', required=False),
        'note': fields.text('Note'),
        'image': fields.binary("Photo",help="Equipment Photo, limited to 1024x1024px."),

        #Applications Page
        'application_ids': fields.many2many('it.application','equipment_application_rel','equipment_id','application_id','Applications'),

        # Config Page
        'equipment_type': fields.selection([('bundle','BUNDLE'),('virtual','VIRTUAL'),('product','PRODUCT'),('other','OTHER')],'Equipment Type',required=True),
        'is_contracted': fields.boolean('Contracted Service'),
        'is_static_ip': fields.boolean('Static IP'),
        'is_partitioned': fields.boolean('Partitions'),
        'is_backup': fields.boolean('Backup'),
        'is_access': fields.boolean('Access'),
        'is_os': fields.boolean('Operating System'),
        'is_application': fields.boolean('Applications'),

        # Config Page - Functions
        'function_dc': fields.boolean('Domain Controller'),
        'function_fileserver': fields.boolean('File Server'),
        'function_host': fields.boolean('Host'),
        'function_router': fields.boolean('Router'),
        'function_database': fields.boolean('Database Server'),
        'function_vpn': fields.boolean('VPN Server'),
        'function_firewall': fields.boolean('Firewall & Proxy Server'),
        'function_dhcp': fields.boolean('DHCP Server'),
        'function_ap': fields.boolean('Access Point'),

        # Audit Page
        'creation_date': fields.date('Creation Date',readonly=True),
        'user_id': fields.many2one('res.users', 'Created by',readonly=True),
        'pin': fields.char('PIN', readonly=True, required=True),

        # Changes Page
        'change_ids': fields.one2many('it.equipment.change','equipment_id','Changes on this equipment'),

        # Contract Page
        'contract_partner_id': fields.many2one('res.partner', 'Contractor', domain="[('supplier','=',1)]"),
        'contract_client_number': fields.char('Client Nummber'),
        'contract_owner': fields.char('Titular'),
        'contract_nif': fields.char('NIF'),
        'contract_direction': fields.char('Invoice Direction'),

        # Virtual Machine Page
        'virtual_parent_id': fields.many2one('it.equipment', 'Equipment', domain="[('function_host','=',1)]"),
        'virtual_memory_amount': fields.char('Memory'),
        'virtual_disk_amount': fields.char('Disk Size'),
        'virtual_processor_amount': fields.char('Number of Processor'),
        'virtual_network_amount': fields.char('Number of Network'),

        # Partition Page
        'partitions_ids': fields.one2many('it.equipment.partition','equipment_id','Partition on this equipment'),

        # Router Page
        'router_dmz': fields.char('DMZ'),
        'router_forward_ids': fields.one2many('it.equipment.forward','equipment_id','Forward Rules'),
        'router_nat_ids': fields.one2many('it.equipment.nat','equipment_id','NAT Rules'),
        'router_rules_ids': fields.one2many('it.equipment.rule','equipment_id','Rules Registry'),

        # Network Configuration Page
        'equipment_network_ids': fields.one2many('it.equipment.network','equipment_id','Network on this equipment'),

        # Physical Page
        'physical_component_ids': fields.one2many('it.equipment.component','equipment_id','Components on this equipment'),

        # Product Page
        'product_id': fields.many2one('product.product', 'Product'),
        'product_serial_number': fields.char('Serial Number'),
        'product_warranty': fields.char('Warranty'),
        'product_buydate': fields.date('Buy Date'),
        'product_note': fields.text('Note'),

        # DC Page
        'dc_name': fields.char('Domain Name'),
        'dc_type': fields.selection([('primary','PRIMARY'),('secundary','SECUNDARY'),('slave','SLAVE')],'DC Type'),
        'dc_user_ids': fields.one2many('it.equipment.dcuser','equipment_id','Users'),
        'dc_group_ids': fields.one2many('it.equipment.dcgroup','equipment_id','Groups'),

        # Fileserver Page
        'equipment_mapping_ids': fields.one2many('it.equipment.mapping','equipment_id','Mappings'),

        # OS Page
        'os_name': fields.char('Name'),
        'os_company': fields.char('Company'),
        'os_version': fields.char('Version'),

        #DHCP Server Page
        'dhcp_scope': fields.char('Scope'),
        'dhcp_relay': fields.char('DHCP Relay'),
        'dhcp_reservation_ids': fields.one2many('it.equipment.ipreservation','equipment_id','Reservations'),

        #Access Point Page
        'ap_ssid': fields.char('SSID'),
        'ap_auth_type': fields.selection([('none','NONE'),('wep64','WEP-64bits'),('wep128','WEP-128bits'),
                                        ('wpa_tkip','WPA-TKIP'),('wpa_aes','WPA-AES'),('wpa2_aes','WPA-AES')
                                        ,('other','OTHER')],'Authentication Type'),
        'ap_password': fields.char('Password'),
        'ap_guest': fields.boolean('Enable Guest Access'),
        'ap_guest_ssid': fields.char('Guest SSID'),
        'ap_guest_password': fields.char('Guest Password'),

        #Database Page
        'db_engine': fields.char('Database Engine'),
        'db_setting_ids': fields.one2many('it.equipment.dbsetting','equipment_id','DB Settings'),
        'db_ids': fields.one2many('it.equipment.db','equipment_id','Databases'),

        #Firewall & Proxy Page
        'firewall_filter_ids': fields.one2many('it.equipment.firewallfilter','equipment_id','Firewall Filters'),
        'proxy_transparent': fields.boolean('Transparent Proxy'),
        'proxy_enable_ssk': fields.boolean('Proxy Enable Single Sign-On (Kerberos)'),
        'proxy_adblocking': fields.boolean('Proxy Ad Blocking'),
        'proxy_port': fields.char('Proxy Port'),
        'proxy_cache_size': fields.char('Proxy Cache File Size'),

        #VPN Page
        'vpn_protocol': fields.selection([('tcp','TCP'),('udp','UDP')],'VPN Protocol'),
        'vpn_address': fields.char('VPN Address'),
        'vpn_server_cert': fields.binary('VPN Server Certificate'),
        'vpn_cacn': fields.boolean('Client Authorization by common name'),
        'vpn_tun': fields.boolean('VPN Tun Interface'),
        'vpn_nat': fields.boolean('VPN Network Address Traslation'),
        'vpn_c2c': fields.boolean('VPN Allow Client to Client connections'),
        'vpn_gateway': fields.boolean('Redirect Gateway'),
        'vpn_search_domain': fields.char('VPN Search Domain'),
        'vpn_wins_server': fields.char('VPN WINS Server'),


    }

    def _get_default_image(context=None):
        image_path = addons.get_module_resource('it', 'static/src/img/', 'default_image_equipment.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    _defaults = {

        'pin': _get_pin,
        'function_router': False,
        'function_host': False,
        'equipment_type': 'bundle',
        'is_static_ip': False,
        'is_partitioned': False,
        'is_backup': False,
        'is_access': False,
        'is_os': False,
        'is_application': False,
        'function_dc': False,
        'function_fileserver': False,
        'function_database': False,
        'function_vpn': False,
        'function_firewall': False,
        'function_dhcp': False,
        'function_ap': False,
        'ap_guest': False,
        'proxy_transparent': False,
        'proxy_enable_ssk': False,
        'proxy_adblocking': False,
        'vpn_cacn': False,
        'vpn_tun': False,
        'vpn_nat': False,
        'vpn_c2c': False,
        'vpn_gateway': False,
        'image': _get_default_image(),
        'active': True,
        'creation_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'user_id': lambda self, cr, uid, ctx: uid,
        'company_id': lambda self,cr,uid,ctx: self.pool['res.company']._company_default_get(cr,uid,object='it.equipment',context=ctx),

    }

    _sql_constraints = [

        ('name_uniq','unique(pin)', 'PIN must be unique!')

    ]

it_equipment()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
