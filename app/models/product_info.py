# -*- coding: utf-8 -*-
from . import db, AppModel

class Product_info(AppModel):
    __tablename__ = 'product_info'
    product_code = db.Column(db.String(16))
    product_name = db.Column(db.String(20), nullable=False)
    product_enname = db.Column(db.String(20),nullable= False)
    # bar_code = db.Column(db.String(50))
    audit_status = db.Column(db.Boolean)
    publish_status  = db.Column(db.Boolean)
    brad_id = db.Column(db.Integer,db.ForeignKey('brand_info.id'))
    cat_id = db.Column(db.Integer,db.ForeignKey('product_category.id'))
    shop_id = db.Column(db.Integer, db.ForeignKey('shop_info.id'))
    # sku_price_id = db.Column(db.Integer, db.ForeignKey('sku_price.id'))
    sku_price = db.relationship('Sku_price', backref = 'product_info', lazy = 'dynamic')

    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse_product.id'))


    def __init__(self, product_name, product_enname, publish_status,
                 brad_info,category, shop,  warehouse_info):
        # self.product_code = product_code
        self.product_name = product_name
        self.product_enname = product_enname
        # self.bar_code = bar_code
        self.publish_status = publish_status
        self.brad_info = brad_info
        self.category = category
        self.shop = shop
        # self.sku_price = sku_price
        self.warehouse_info = warehouse_info

    def __repr__(self):
        return '{}'.format(self.product_name)
