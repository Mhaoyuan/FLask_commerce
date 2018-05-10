# -*- coding: utf-8 -*-
from flask import Blueprint, session,escape
from flask_security import current_user
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'hello world'
@main.route('/user')
def user():
    # email = session['email']
    # return "{}".format(email)
    return 'hello, {}\n'.format(escape(session['user.id']))