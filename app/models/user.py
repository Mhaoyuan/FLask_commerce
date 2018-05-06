# -*- coding: utf-8 -*-
from flask_security import UserMixin
from . import db, AppModel, roles_users
from .role import Role
from flask import current_app
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

class User(AppModel,UserMixin):

    # __tablename__ = 'user'
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), unique= True, index= True)
    phone = db.Column(db.Integer(),unique=True, index= True)
    roles = db.relationship('Role', secondary = roles_users,
                            backref = db.backref('users', lazy = 'dynamic'))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer())
    shop_status = db.Column(db.String(128)) # 未申请 审核中 已通过
    addr = db.relationship('Addr',backref = 'users', lazy = 'dynamic')
    point_log = db.relationship('Point_Log', backref = 'users', lazy = 'dynamic')
    balance_log = db.relationship('Balance_Log', backref = 'users', lazy = 'dynamic')
    login_log = db.relationship('Login_Log', backref = 'users', lazy = 'dynamic')
    shop_info = db.relationship('Shop_Info', backref = 'users',lazy = 'dynamic')
    order_master = db.relationship('Order_master', backref = 'users', lazy = 'dynamic')


    def __init__(self ,email,active,password,roles  ):
        # self.phone = phone
        # self.username = username
        self.email = email
        self.active = active
        self.password = password
        self.roles =roles

    def __repr__(self):
        return '{}'.format(self.email)

    @staticmethod
    def generate_auth_token(self, expiration = 3600):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'id':self})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user


