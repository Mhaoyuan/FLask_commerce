# -*- coding: utf-8 -*-
from flask import redirect,request, url_for
from flask_security import current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import  SQLAlchemy
from app.models import db
from app.models.user import User
from app.models.role import Role
from app.models.shop_info import Shop_Info
from app.models.customer_addr import Addr
from app.models.prouduct_info import Product_info
from app.models.brand_info import Brand_info
from app.models.sku_price import Sku_price
from app.models.product_category import Product_Category
class AppModelView(ModelView):
    # def is_accessible(self):
    #     pass
    def is_accessible(self):
        return current_user.has_role('Admin')
    def inaccessible_callback(self, name, **kwargs):
        redirect(url_for("security.login", next = request.url))







admin = Admin(name='home',base_template="app_master.html",template_mode="bootstrap3")

from .user import UserModelView





admin.add_view(UserModelView(User, db.session, name = u'用户'))
admin.add_view(ModelView(Shop_Info, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Addr,db.session))
admin.add_view(ModelView(Product_Category,db.session))
admin.add_view(ModelView(Product_info,db.session))
admin.add_view(ModelView(Brand_info,db.session))
admin.add_view(ModelView(Sku_price,db.session))
