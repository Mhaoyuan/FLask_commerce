# -*- coding: utf-8 -*-
from . import db, AppModel

class Sku_price(AppModel):
    __tablename__ = 'sku_price'
    mass = db.Column(db.String(16))
    purer = db.Column(db.String(16))
    price = db.Column(db.Integer)
    product_info = db.relationship('Product_info', backref = 'sku_price', lazy = 'dynamic')

    def __init__(self,mass,purer,price):
        self.mass = mass
        self.purer = purer
        self.price = price

    def __repr__(self):
        return '{}'.format(self.price)