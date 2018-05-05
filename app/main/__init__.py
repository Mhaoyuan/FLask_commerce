# -*- coding: utf-8 -*-
from flask import Blueprint, g
from flask_security import current_user
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'hello world'
@main.route('/user')
def user():
    id = current_user.id

    return "{}".format(id)