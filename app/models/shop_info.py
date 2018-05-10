# -*- coding: utf-8 -*-
from . import db, AppModel

class Shop_Info(AppModel):
    __tablename__ = 'shop_info'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    shop_code = db.Column(db.String(128))
    shop_name = db.Column(db.String(128), nullable = False)
    shop_type = db.Column(db.String(16), nullable= False)
    link_man = db.Column(db.String(10), nullable= False)
    phone_number = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(16))
    state = db.Column(db.String(16))
    city = db.Column(db.String(16))
    address = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean(), default=0, nullable=False) #0:不可用，1：可用
    product_info = db.relationship('Product_info', backref = 'shop', lazy = 'dynamic')

    # def __repr__(self):
        # return '<Suppier_Info % >' % self.supplier_name
    def __init__(self,users,shop_name,shop_type,
                link_man, phone_number,country, state,
                 city, address):
        self.users= users
        # self.supplier_code = shop_code
        self.shop_name= shop_name
        self.shop_type = shop_type
        self.link_man = link_man
        self.phone_number = phone_number
        self.country = country
        self.state = state
        self.city = city
        self.address = address

    def __repr__(self):
        return '{}'.format(self.shop_name)

