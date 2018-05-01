# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader

from odoo import http
from odoo.http import request
import simplejson
import logging
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
template_loader = FileSystemLoader(searchpath=BASE_DIR + "/template/carrier/")
jinja = Environment(loader=template_loader)

_logger = logging.getLogger(__name__)


class StudentPageController(http.Controller):
    #登录验证
    @http.route('/api/login_auth', auth='none', csrf=False)
    def carrier_login_auth(self, **post):
        result = {}
        uid = 1
        # try:
        #     if request.httprequest.method == 'GET':
        #         return jinja.get_template("login.html").render()
        #     if request.httprequest.method == 'POST':
        #         uid = request.session.authenticate(request.session.db, str(post.get('username')),
        #                                            str(post.get('password')))
        if uid:
            result.update({
                'code': 1,
                'msg': u'登陆成功',
            })
        else:
            result.update({
                'code': 0,
                'msg': u'登陆失败',
            })
            return http.Response(simplejson.dumps(result), status=400)
        return http.Response(simplejson.dumps(result), status=200)