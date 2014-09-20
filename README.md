# ODOO INFRASTRUCTURE MODULE

This module is used for Infrastructure management. You can registry several types of equipments, access, and backups. 


## EQUIPMENTS

![Alt Text](/docs/img/server_example.jpg?raw=true "Server Example").

### GENERAL DATA FOR EQUIPMENTS
* Identification ( Owner - Name )
* Name
* Description
* Owner
* Functions ( tags )
* Changes.
* Creation Audit data.
  * User
  * Date
* Notes

### GENERAL CONFIGURATION FOR EQUIPMENTS
* Active: For openerp struct data.
* Company: Filtered for non multicompany users.
* Contracted Service : Add page for contract data.
* DHCP: For equipments without network config. Delete network configuration page.
* Disk and Partitions: Add page disk and partition page. Where can registry disk, formats, and mounts.
* Access: Add button "Access" on righttop corner. 
* Backup: Add button "Backups" on righttop corner.
* Operational System: Add operational system page where can registry name, company , and version.
* Equipment type:
  * Physical: For example: servers, this type add page for physical nformation
  * Virtual: Add page for virtual machine data as host, mem, disk size, quantity of processors, number of networks
  * Other: Example for printers, switch, router , etc


###FUNCTIONS CONFIGURATION

* Host: Add button "Virtuals" on righttop corner. 
* Router:Add page for contract data.
![Alt text](/docs/img/router_example.jpg?raw=true "Router Example").
* Domain Controller: Add page for domain data.
* Fileserver: Add page for fileserver where can registry mappings and permissions.


## ACCESS

![Alt text](/docs/img/access_example.jpg?raw=true "Access Example")

### GENERAL DATA FOR ACCESS
* Name
* Equipment
* Owner ( Related to equipment)
* Note
* Information Page
  * User
  * App
  * Desc
  * Password
  * Port
  * Link
*SSL Page ( binaries)
  * CSR 
  * CRT
  * PUBLIC KEY
  * PRIVATE KEY
* Creation Audit data
  * User
  * Date


## BACKUPS

![Alt text](/docs/img/backup_example.jpg?raw=true "Backup Example")	

### GENERAL DATA FOR BACKUPS
* Name
* Equipment
* Owner ( Related to equipment)
* Type
  * FULL
  * DIFF
  * INCREMENTAL
  * OTHER
* Note
* Information Page
  * Destination
  * Origin
  * Script ( binary)
  * Frecuency
  * Time
  * Script location
* Creation Audit data
  * User
  * Date


## ROLES:
Restrictc menu, equipment, access and backups, etc.
* User ( 1,0,0,0)
* Moderator (1,1,1,0)
* Manager (1,1,1,1)
      
## PARTNERS
Quick data access from partners.

![Alt text](/docs/img/partner_example.jpg?raw=true "Partner Example")


# TODO LIST
- [x] Change Readme.
- [x] Change nat, forwards and rules model and view.
- [ ] Add applications model (software).
- [ ] Think about configuration page and all posibles configuration.
- [ ] More information for printers and other devices.
- [ ] Fix View of server changes.
