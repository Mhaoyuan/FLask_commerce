# -*- coding: utf-8 -*-
from . import db,AppModel

class Point_Log(AppModel):
    __tablename__ = 'customer_point_log'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    source = db.Column(db.SmallInteger) #积分来源0：订单 1：登录2：活动
    refer_number = db.Column(db.Integer)#积分来源编号
    change_point = db.Column(db.Integer)#变化积分数


