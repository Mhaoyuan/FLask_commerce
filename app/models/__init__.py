# -*- coding: utf-8 -*-
from sqlalchemy.sql import func

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()
class AppModel(db.Model):
    __abstract__ = 1
    id = db.Column(db.Integer(), primary_key=1)
    create_datetime = db.Column(db.DateTime(), default= func.now())
    update_datetime = db.Column(db.DateTime(), default=func.now())

    def ping(self):
        self.update_datetime =datetime.utcnow()
        db.session.add(self)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self, depth = 1, include = None):
        if not include: include = list()

        if depth:
            depth -=1
            exclude = ["create_datetime", "update_datetime", "role", "password",
                       "active", "confirmed", "confirmed_at", "current_login_at",
                       "login_count", "last_login_ip", "current_login_ip"]
            attrs = self.__mapper__.attrs.keys()
            relationships = self.__mapper__.relationships.keys()
            columns = [item for item in [cols for cols in attrs if cols not in relationships] if item not in exclude]
            relationships = [item for item in self.__mapper__.relationships.keys() if item in include]
            dictionary = {column : getattr(self, column) for column in columns}

            for relationship in relationships:
                related = getattr(self, relationship)

                if related:
                    is_list = self.__mapper__.relationships[relationship].uselist

                    if is_list:
                        # dictionary[relationship] = [record.to_dict(depth, include) for record in related]
                        dictionary[relationship] = [record.to_dict(depth, include) for record in related]

                    else:
                        dictionary[relationship] = related.to_dict(depth, include)

            return dictionary
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


from .role import Role
from .user import User
from .customer_point_log import Point_Log
from .customer_balance_log import Balance_Log
from .customer_login_log import Login_Log
from .shop_info import Shop_Info
from .customer_addr import Addr
from .prouduct_info import Product_info
from .product_category import Product_Category
from .order_master import Order_master

