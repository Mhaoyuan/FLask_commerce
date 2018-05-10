# -*- coding: utf-8 -*-
from . import db,AppModel

class Warehouse_info(AppModel):
    __tablename = 'warehouse_info'
    warehouse_name = db.Column(db.String(128),nullable=False)
    warehouse_phone = db.Column(db.String(128),nullable=False)
    link_man = db.Column(db.String(128),nullable=False)
    state = db.Column(db.String(128),nullable=False)
    city = db.Column(db.String(128), nullable= False)
    area = db.Column(db.String(128), nullable=False)
    street = db .Column(db.String(128), nullable=False)


    def __init__(self,warehouse_name, warehouse_phone,
                 link_man, state, city, area, street):
        self.warehouse_name = warehouse_name
        self.warehouse_phone = warehouse_phone
        self.link_man = link_man
        self.state = state
        self.city = city
        self.area = area
        self.street = street

    def __repr__(self):
        return '{}'.format(self.warehouse_name)





