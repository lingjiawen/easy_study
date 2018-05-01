#!/usr/bin/env python

# set server timezone in UTC before time module imported
# use: python start.py -c config/prod.conf
import os
import sys
sys.setrecursionlimit(99999)

LIB_PATH = os.path.join(os.path.dirname(__file__), '.', 'odoo')
sys.path.append(LIB_PATH)

__import__('os').environ['TZ'] = 'UTC'
__import__('pkg_resources').declare_namespace('odoo.addons')

import odoo

if __name__ == "__main__":
    from odoo.modules.module import (
        load_openerp_module,
    )
    load_openerp_module('web')
    odoo.cli.main()
