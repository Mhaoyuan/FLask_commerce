# -*- coding: utf-8 -*-
from . import db, AppModel

class Product_Category(AppModel):
    __tablename__ = 'product_category'
    category_name = db.Column(db.String(10),nullable=False)
    # category_code = db.Column(db.String(10),nullable=False)
    parent_id = db.Column(db.SmallInteger)
    # category_level = db.Column(db.SmallInteger)
    category_status = db.Column(db.SmallInteger,default=1)
    product_info = db.relationship('Product_info', backref = 'category',lazy = 'dynamic')
    def __repr__(self):
        return '<Product_CateGory %r>' % self.category_name

    def __init__(self,category_name,parent_id):
        self.category_name = category_name
        self.parent_id = parent_id


