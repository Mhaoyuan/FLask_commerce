# -*- coding: utf-8 -*-
from . import db, AppModel

class Product_info(AppModel):
    __tablename__ = 'product_info'
    product_code = db.Column(db.String(16), nullable=False)
    product_name = db.Column(db.String(20), nullable=False)
    product_enname = db.Column(db.String(20),nullable= False)
    bar_code = db.Column(db.String(50))
    audit_status = db.Column(db.Boolean)
    publish_status  = db.Column(db.Boolean)
    brad_id = db.Column(db.Integer,db.ForeignKey('brand_info.id'))
    cat_id = db.Column(db.Integer,db.ForeignKey('product_category.id'))
    shop_id = db.Column(db.Integer, db.ForeignKey('shop_info.id'))
    sku_price_id = db.Column(db.Integer, db.ForeignKey('sku_price.id'))
    # werehouse_product = db.Column(db.Integer, db.ForeignKey('werehouse_product.id'))


    def __init__(self,product_code, product_name, product_enname,bar_code, publish_status,
                 brad_id,cat_id, shop_id, sku_price_id):
        self.product_code = product_code
        self.product_name = product_name
        self.product_enname = product_enname
        self.bar_code = bar_code
        self.publish_status = publish_status
        self.brad_id = brad_id
        self.cat_id = cat_id
        self.shop_id = shop_id
        self.sku_price_id = sku_price_id