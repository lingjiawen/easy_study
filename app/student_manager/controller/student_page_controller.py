# -*- coding: utf-8 -*-
import os
import time
from jinja2 import Environment, FileSystemLoader
from odoo import http
from odoo.http import request
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
template_loader = FileSystemLoader(searchpath=BASE_DIR + "/template/student/")
jinja = Environment(loader=template_loader)

_logger = logging.getLogger(__name__)


class StudentAPIController(http.Controller):
    @http.route('/login', auth='none', csrf=False)
    def student_login(self, **post):
        template = jinja.get_template("login.html")
        return template.render()

    @http.route('/main', auth='none', csrf=False)
    def student_main(self, **post):
        template = jinja.get_template("main.html")
        return template.render()

    @http.route('/change_password', auth='none', csrf=False)
    def student_change_password(self, **post):
        template = jinja.get_template("change_password.html")
        return template.render()

    @http.route('/new_friend', auth='none', csrf=False)
    def student_new_friend(self, **post):
        template = jinja.get_template("new_friend.html")
        return template.render()

    @http.route('/contact_detail', auth='none', csrf=False)
    def student_contact_detail(self, **post):
        template = jinja.get_template("contact_detail.html")
        return template.render()

    @http.route('/student_information', auth='none', csrf=False)
    def student_information(self, **post):
        template = jinja.get_template("student_information.html")
        return template.render()

    @http.route('/course_detail', auth='none', csrf=False)
    def student_course_detail(self, **post):
        template = jinja.get_template("course_detail.html")
        return template.render()

    @http.route('/student_information_school', auth='none', csrf=False)
    def student_information_school(self, **post):
        template = jinja.get_template("student_information_school.html")
        return template.render()

    @http.route('/student_information_grade', auth='none', csrf=False)
    def student_information_grade(self, **post):
        template = jinja.get_template("student_information_grade.html")
        return template.render()

    @http.route('/student_information_signature', auth='none', csrf=False)
    def student_information_signature(self, **post):
        template = jinja.get_template("student_information_signature.html")
        return template.render()