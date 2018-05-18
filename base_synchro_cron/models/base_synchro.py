# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

import logging
import threading
import time
import xmlrpclib

from odoo import models, fields, api
from odoo.exceptions import Warning
from odoo.tools.translate import _
class BaseSynchro(models.Model):
    """Base Synchronization."""

    _name = 'base.synchro.setting'

    server_url = fields.Many2one('base.synchro.server', "Server URL", required=True)
    user_id = fields.Many2one('res.users', "Send Result To", default=lambda self: self.env.user)

    @api.multi
    def process_sync_cron(self):
        wz = self.env['base.synchro']
        settings = self.search([])
        for setting in settings:
            sync = wz.create({'server_url': setting.server_url.id, 'user_id': setting.user_id.id})
            sync.upload_download_multi_thread()
