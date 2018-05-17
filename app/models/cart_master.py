# -*- coding: utf-8 -*-
from flask import request,jsonify
from . import db, AppModel
from .cart_detail import Cart_detail
from .user import User

class Cart_master(AppModel):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cart_detail = db.relationship('Cart_detail', backref = 'cart_master',lazy = 'dynamic')
    total = db.Column(db.Integer())
    price = db.Column(db.Integer(),default=0)

    def __init__(self,user):
        self.users = user


    def __repr__(self):
        return '{}'.format(self.price)

    def update_total_price(self):
        self.total = Cart_detail.query.filter_by(cart_master = self).count()
        cart_detail = Cart_detail.query.filter_by(cart_master = self).all()
        self.price = 0
        for item in cart_detail:
            self.price += item.price







