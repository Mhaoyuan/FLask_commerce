# -*- coding: utf-8 -*-
from flask import request,json, Response, jsonify,abort, url_for,redirect,g
from flask_security import login_user, auth_token_required
from flask_security.utils import hash_password,verify_password
from . import api
from ..models import db
from ..models import User
@api.route('/login', methods = ['POST'])
def sigin():
    phone = request.json.get("phone")
    password = request.json.get("password")
    remeber_me = request.json.get('remeber_me')
    user = User.query.filter_by(phone = phone).first()
    if user is not None and verify_password(password,user.password):
        login_user(user, remeber_me)
        g.user = user
        return jsonify({'user_id':user.id,'token':user.get_auth_token()}),201
    return jsonify(401)

@api.route('/register', methods = ['POST'])
def new_user():
    phone = request.json.get('phone')
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')



    if phone is None or password is None:
        abort(400)
    if User.query.filter_by(phone = phone).first() is not None:
        abort(400)
    user = User(phone = phone, username=username, email=email)
    # a = hash_password(password)
    # user.hash_password =a
    user.password = hash_password(password)
    # user.password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'phone': user.phone}),201)

@api.route('/password', methods = ['POST'])
@auth_token_required
def change_password():
    old_password = request.json.get('old_password')
    password = request.json.get('password')


@api.route('/protect', methods = ['GET'])
@auth_token_required
# @http_auth_required
# @login_required
def index():
    return "hello world"

