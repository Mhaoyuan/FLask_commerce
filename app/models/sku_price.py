# -*- coding: utf-8 -*-
from . import db, AppModel

class Sku_price(AppModel):
    __tablename__ = 'sku_price'
    mass = db.Column(db.String(16))
    purer = db.Column(db.String(16))
    price = db.Column(db.Integer)
    cart_detail = db.relationship('Cart_detail', backref = 'sku', lazy = 'dynamic')
    product_id  = db.Column(db.Integer, db.ForeignKey('product_info.id'))
    def __init__(self,mass,purer,price, product_info):
        self.mass = mass
        self.purer = purer
        self.price = price
        self.product_info = product_info

    def __repr__(self):
        return '{}'.format(self.price)