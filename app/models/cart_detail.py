# -*- coding: utf-8 -*-

from . import db, AppModel

class Cart_detail(AppModel):
    master_id = db.Column(db.Integer, db.ForeignKey('cart_master.id'))
    sku_id = db.Column(db.Integer(), db.ForeignKey('sku_price.id'))
    quantity = db.Column(db.Integer())
    product_name = db.Column(db.String(128))
    price = db.Column(db.Integer())

    def __init__(self, cart_master, sku,quantity,
                 product_name,price=0):
        self.cart_master =cart_master
        self.sku = sku
        self.quantity = quantity
        self.product_name = product_name
        self.price = price

    def update_price(self):
        price = self.sku.price*self.quantity
        return price
    # def item_dict(self):
    #     return {item.sku.id: item for item in self}

