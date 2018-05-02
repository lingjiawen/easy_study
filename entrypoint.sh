#! /bin/bash
set -e
exec gosu odoo python /code/start.py -c /code/config/prod.conf
