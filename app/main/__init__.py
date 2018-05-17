# -*- coding: utf-8 -*-
from flask import Blueprint, session,escape,request
from flask_security import current_user
from app.models.user import User
from app.models import db
from app.models.sku_price import Sku_price
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'hello world'
@main.route('/user',methods = ['GET'])
def user():
    # email = session['email']
    # return "{}".format(email)
    # use_id = current_user._get_current_object().id
    # for i in session:

    # return 'hello, {}\n'.format(session.get('token'))
    # user = User.query.filter_by(id=2).first()
    # db.session.add(user)
    # sess = session['']
    # session['cart'] = {'sku':"as"}
    # session.modified = True
    # return '{}'.format(session.items())
    # sku = Sku_price.query.filter_by().all()
    user = current_user._get_current_object()
    pass
