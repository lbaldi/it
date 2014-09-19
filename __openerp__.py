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

{

    'name': 'Infrastructure',

    'version': '2.0',

    'depends': ['base','product'],

    'author': 'Leandro Ezequiel Baldi <baldileandro@gmail.com>',
    
    'license': 'AGPL-3',

    'category': 'Infrastructure',

    'description': """
    
    This module is used for Infrastructure management.
    
		Objects and model:
			- Equipments
			- Access
			- Backups
		
		Three roles and multicompany security:
			- User ( 1,0,0,0)
			- Moderator (1,1,1,0)
			- Manager (1,1,1,1)
        
        Equipments in general as:
			- Physical Servers
			- Virtual Servers
			- Router
			- Switchs
			- Printers
			
		Equipment configuration:
			- Contracted Service
			- DHCP
			- Disk and Partitions
			- Access
			- Backup
			- Operational System
			- Equipment type:
				- Physical
				- Virtual
				- Other
		
		Equipment functions configuration:
			- Host
			- Router
			- Domain Server
			- File Server
			
		Depends on the configurations equipments have differents pages:
			- Disk and Partitions
			- Physical Information
			- Contract Service Information
			- Router and Switch Configuration
			- Network Configuration
			- File Server
			- Virtual Machine Data
			- Domain Controller
			- Operational System
			- Changes		
    """,

    'images': [
    
        'static/src/img/default_image_equipment.png',
        
    ],

    'data': [
        
        'security/it_security.xml',
        'security/ir.model.access.csv',
        'views/it_menu_view.xml',
        'views/equipment_view.xml',
        'views/equipment_change_view.xml',
        'views/equipment_component_view.xml',
        'views/equipment_network_view.xml',
        'views/equipment_rule_view.xml',
        'views/equipment_nat_view.xml',
        'views/equipment_forward_view.xml',
        'views/equipment_partition_view.xml',
        'views/component_view.xml',
        'views/access_view.xml',
        'views/partner_view.xml',
        'views/backup_view.xml',
        'views/equipment_function_view.xml',
        'views/equipment_mapping_view.xml',
    
    ],

    'demo': [
        #files containg demo data
    ],

    'test': [
        #files containg tests
     ],
     
    'auto_install': False,

    'installable': True,

}
