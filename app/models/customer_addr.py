# -*- coding: utf-8 -*-
from . import db, AppModel, role

class Addr(AppModel):
    __tablename__ = 'customer_addr'
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    name = db.Column(db.String(16))
    telephone = db.Column(db.Integer)
    country = db.Column(db.String(16))
    state = db.Column(db.String(16))
    city = db.Column(db.String(16))
    area = db.Column(db.String(16))
    street = db.Column(db.String(16))
    default = db.Column(db.Boolean)
    zip = db.Column(db.Integer)
    order_master = db.relationship('Order_master', backref = 'addr', lazy = 'dynamic')
    # province = db.Column(db.String())

    def __init__(self, name, telephone, country, state, city,
                 area, street, default, zip,user_id):
        self.name = name
        self.telephone = telephone
        self.country = country
        self.state = state
        self.city = city
        self.area = area
        self.street = street
        self.default = default
        self.zip = zip
        self.user_id = user_id