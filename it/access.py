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
import random
import base64
from random import choice
from openerp import addons, tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class it_access(osv.osv):

    _name = "it.access"

    _description = "Access"

    def onchange_equipment(self, cr, uid, ids, equipment_id, context=None):
        if equipment_id:
            equipment_obj = self.pool.get('it.equipment')
            equipment_inst = equipment_obj.browse(cr, uid, equipment_id, context=context)
            return {'value':{'partner_id': equipment_inst.partner_id.id }}
        return False

    def get_random_password(self, cr, uid, ids, context=None):
        for access in self.browse(cr, uid, ids, context=context):
            longitud = 16
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
            p = ""
            p = p.join([choice(valores) for i in range(longitud)])
            self.write(cr, uid, ids, {'password': p, 'encrypted': False })
        return True

    def onchange_password(self, cr, uid, ids, encrypted, context={}):
        return {'value':{'encrypted': False}}


    def encrypt_password(self, cr, uid, ids, *args):
        try:
            from Crypto.Cipher import ARC4
        except ImportError:
            raise osv.except_osv(_('Error !'), _('Package python-crypto no installed.'))
                
        val = self.pool.get('ir.config_parameter').get_param(cr, uid, 'it_passkey')
        if not val:
            raise osv.except_osv(_('Error !'), _('For Encryptation you must set a system parameter with key "it_passkey" and fill in value a passkey'))
            
        for rec in self.browse(cr, uid, ids):

            if not rec.encrypted:
                enc = ARC4.new(val)
                try:
                    encripted = base64.b64encode(enc.encrypt(rec.password))
                except UnicodeEncodeError:
                    break
                self.write(cr, uid, [rec.id], {'password': encripted, 'encrypted': True})
            else:
                raise osv.except_osv(_('Error !'), _('Password already encrypted'))
            
        return True


    def decrypt_password(self, cr, uid, ids, *args):
        try:
            from Crypto.Cipher import ARC4
        except ImportError:
            raise osv.except_osv(_('Error !'), _('Package python-crypto no installed.'))
                
        val = self.pool.get('ir.config_parameter').get_param(cr, uid, 'it_passkey')
        if not val:
            raise osv.except_osv(_('Error !'), _('For Encryptation you must set a system parameter with key "it_passkey" and fill in value a passkey'))
            
        for rec in self.browse(cr, uid, ids):
            dec = ARC4.new(val)
            try:
                desencripted = dec.decrypt(base64.b64decode(rec.password))
                unicode(desencripted, 'ascii')
                raise osv.except_osv(_('Decrypt password:'), desencripted)
            except UnicodeDecodeError:
                raise osv.except_osv(_('Error !'), _('Wrong encrypt/decrypt password.'))

        return True

    _columns = {

        'name': fields.char('Name', size=64, required=True),
        'company_id': fields.many2one('res.company', 'Company', required=True),
        'equipment_id': fields.many2one('it.equipment', 'Equipment', domain="[('is_access','=',1)]", ondelete='cascade'),
        'user_id': fields.many2one('res.users', 'Created by', readonly=True),
        'application': fields.char('Application', size=64),
        'user': fields.char('User', size=64),
        'password': fields.char(string='Password'),
        'encrypted': fields.boolean('Encrypted'),
        'port': fields.char('Port'),
        'partner_id': fields.many2one('res.partner', 'Partner', required=True, domain="[('manage_it','=',1)]"),
        'description': fields.char('Description', size=120),
        'link': fields.char('Link', size=120),
        'creation_date': fields.date('Creation Date',readonly=True),
        'active': fields.boolean('Active'),
        'ssl_csr': fields.binary('CSR',filters='*.csr', filename="ssl_csr_filename"),
        'ssl_csr_filename': fields.char('CSR Filename'),
        'ssl_cert': fields.binary('Cert',filters='*', filename="ssl_cert_filename"),
        'ssl_cert_filename': fields.char('Cert Filename'),
        'ssl_publickey': fields.binary('Public Key',filters='*', filename="ssl_publickey_filename"),
        'ssl_publickey_filename': fields.char('Public Key Filename'),
        'ssl_privatekey': fields.binary('Private Key',filters='*', filename="ssl_privatekey_filename"),
        'ssl_privatekey_filename': fields.char('Private Key Filename'),
        'note': fields.text('Note'),

    }

    _defaults = {
        'encrypted': False,
        'creation_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'active': True,
        'company_id': lambda self,cr,uid,ctx: self.pool['res.company']._company_default_get(cr,uid,object='it.equipment',context=ctx),
        'user_id': lambda self, cr, uid, ctx: uid,

    }

it_access()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
