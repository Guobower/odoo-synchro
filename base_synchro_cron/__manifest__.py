# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    "name": "Multi-DB Synchronization Cron",
    "version": "10.0.1.0.0",
    "category": "Tools",
    "license": "AGPL-3",
    "summary": "Multi-DB Synchronization",
    "description": """ Setting Cron for automate synchronisation """,
    "author": "Cedric FOWOUE",
    'maintainer': 'Cedric FOWOUE',
    "depends": ["base"],
    "website": "",
    "data": [
        "security/ir.model.access.csv",
        "views/base_synchro_view.xml",
        "data/ir_cron.xml",
    ],
    "installable": True,
    "auto_install": False
}
