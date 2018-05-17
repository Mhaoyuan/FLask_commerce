# -*- coding: utf-8 -*-
from flask import redirect,request, url_for
from flask_security import current_user
from flask_admin import Admin,BaseView,expose
from flask_admin.base import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask.ext.admin.base import MenuLink
from app.models import db
from app.models.user import User
from app.models.role import Role
from app.models.shop_info import Shop_Info
from app.models.customer_addr import Addr
from app.models.product_info import Product_info
from app.models.brand_info import Brand_info
from app.models.sku_price import Sku_price
from app.models.product_category import Product_Category
from app.models.cart_master import Cart_master
from app.models.cart_detail import Cart_detail
# from app import admin
class AppModelView(ModelView):
    # def is_accessible(self):
    #     pass
    def is_accessible(self):
        return current_user.has_role('Admin')
    def inaccessible_callback(self, name, **kwargs):
        redirect(url_for("security.login", next = request.url))

class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated

# 定义登录后的MenuLink：
class NotAuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return not current_user.is_authenticated



#主页视图
class MyAdminIndexView(AdminIndexView):
    #增加这个必须要登录后才能访问，不然显示403错误
    #但是还是不许再每一个函数前加上这么判定的  ，不然还是可以直接通过地址访问
    def is_accessible(self):
        return current_user.is_authenticated

    #跳转
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

    #后台首页
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

# admin = Admin(name='chahua3287',index_view=MyAdminIndexView())



admin = Admin(name='home',template_mode="bootstrap3",
              index_view= MyAdminIndexView())
from .user import UserModelView
from .shop import ShopModelView

admin.add_view(UserModelView(User, db.session, name = u'用户管理'))
admin.add_view(ShopModelView(Shop_Info, db.session, name = u'商铺管理'))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Addr,db.session))
admin.add_view(ModelView(Product_Category,db.session))
admin.add_view(ModelView(Product_info,db.session))
admin.add_view(ModelView(Brand_info,db.session))
admin.add_view(ModelView(Sku_price,db.session))
admin.add_link(AuthenticatedMenuLink(name = 'logout',
                                     endpoint='security.logout'))
admin.add_view(ModelView(Cart_master,db.session))
admin.add_view(ModelView(Cart_detail,db.session))
