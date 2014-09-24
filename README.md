# ODOO INFRASTRUCTURE MODULE [v7]

This module is used for Infrastructure management. You can registry several types of equipments, access, backups and applications.


## EQUIPMENTS

![Alt Text](/docs/img/server_example.jpg?raw=true "Server Example")

### GENERAL DATA FOR EQUIPMENTS
* Identification ( Owner - Name )
* Name
* Description
* Owner (required)
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
* Static IP: For equipments without network config. Delete network configuration page.
* Disk and Partitions: Add page disk and partition page where can registry disk, formats, and mounts.
* Access: Add button "Access" on righttop corner.
* Backup: Add button "Backups" on righttop corner.
* Operational System: Add operational system page where can registry name, company , and version.
* Applications: Add page applications where you can registry all software installations (many2many).
* Equipment type:
  * Bundle: For example: servers, this type add page for physical nformation
  * Virtual: Add page for virtual machine data as host, mem, disk size, quantity of processors, number of networks
  * Product: Example for printers, switch, router , etc. Add page to register related product.
  * Other: ...


###FUNCTIONS CONFIGURATION

* Host: Add button "Virtuals" on righttop corner.
* Router: Add page for router configuration.

![Alt text](/docs/img/router_example.jpg?raw=true "Router Example")

* Domain Controller: Add page for domain data.
* Fileserver: Add page for fileserver where can registry mappings and permissions.


## ACCESS

![Alt text](/docs/img/access_example.jpg?raw=true "Access Example")

### GENERAL DATA FOR ACCESS
* Name
* Equipment
* Owner (required)
* Note
* Information Page
  * User
  * App
  * Desc
  * Password
  * Port
  * Link
* SSL Page ( binaries)
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
* Equipment (required)
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

## APPLICATIONS

![Alt text](/docs/img/application_example.jpg?raw=true "Application Example")

### GENERAL DATA FOR APPLICATIONS
* Name
* Developer
* Type
  * OpenSource
  * ClosedSource
* License (abm involve name and a copy of license)
* Link
* Download Link
* Documentation (binary)
* Note
* Equipments (many2many)
* Creation Audit data
  * User
  * Date
* If ClosedSource is selected:
  * Key
  * Keygen (binary)
  * Crack (binary)


## ROLES:
Restrictc menu, equipment, access and backups, etc.
* User ( 1,0,0,0)
* Moderator (1,1,1,0)
* Manager (1,1,1,1)

## PARTNERS
Quick data access from partners.

![Alt text](/docs/img/partner_example.jpg?raw=true "Partner Example")


# TODO LIST
- [x] Add especification to readme and some images.
- [x] Fix default image for servers.
- [x] Change nat, forwards and rules model and view.
- [x] Add applications model (software).
- [x] Domain ons one2many for model
- [x] More information for printers and other devices.
- [x] Fix View of server changes.
- [x] PIN unique for equipment
- [ ] Think about configuration page and all posibles configuration.
- [ ] Test.
- [ ] Travis or runbot integration.
- [ ] Application Bundle for quick config as a template.
- [ ] Buttons on tree view for quick download. (same buttons calls)
- [ ] Demo data
- [ ] Data for licenses.
- [ ] Generate Random Passwords
- [ ] QR image
- [ ] Translation Review
- [ ] IT Client Portal Role
- [ ] Equipment function : Database Server
- [ ] Equipment function : VPN Server
- [ ] Equipment function : Domain Controller - Users table
- [ ] Equipment function : Firewall & Proxy
- [ ] Equipment function : DHCP Server - Scope - Reservation.
- [ ] Equipment function : Router - merge data to DHCP Server
- [ ] Equipment function : Router - SSID WIFI Config for AP
- [ ] Template equipment
- [ ] Partner and equipment buttons counter
- [ ] QR image
