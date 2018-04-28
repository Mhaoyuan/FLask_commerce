from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import  SQLAlchemy
from app.models import db
from app.models.user import User
from app.models.role import Role
from app.models.supplier_info import Supplier_Info
from app.models.customer_addr import Addr
from app.models.product_category import Product_Category
from app.models.prouduct_info import Product_info
from app.models.brand_info import Brand_info
from app.models.sku_price import Sku_price
class AppModelView(ModelView):
    # def is_accessible(self):
    #     pass
    pass







admin = Admin(name='home')

from .user import UserModelView





admin.add_view(UserModelView(User, db.session, name = u'yonghu'))
admin.add_view(ModelView(Supplier_Info, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Addr,db.session))
admin.add_view(ModelView(Product_Category,db.session))
admin.add_view(ModelView(Product_info,db.session))
admin.add_view(ModelView(Brand_info,db.session))
admin.add_view(ModelView(Sku_price,db.session))
