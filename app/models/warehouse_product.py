# -*- coding: utf-8 -*-

from . import db, AppModel

class Warehouse_Product(AppModel):
    __tablename__ = 'warehouse_product'
    current_cnt = db.Column(db.Integer)
    lock_cnt = db.Column(db.Integer)
    in_transit_cnt = db.Column(db.Integer)

    product_info = db.relationship('Product_info', backref = 'warehouse_info', lazy = 'dynamic')


    def __init__(self, current_cnt):
        self.current_cnt = current_cnt

    def __repr__(self):
        return '{}'.format(self.current_cnt)

