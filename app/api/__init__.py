# -*- coding: utf-8 -*-
import traceback
from flask import Blueprint,current_app,abort
from app.models import db
from app.security import user_datastore
from app.models import Product_Category
api = Blueprint('api', __name__)

@api.before_app_first_request
def init_db():
    # try:
    #     roles = ["User", 'Shop', 'Admin']
    #     for r in roles:
    #         role = Role.query.filter_by(name = r).first()
    #         if role is None:
    #             user_datastore.create_role(name = r)
    #             db.session.commit()
    # except InterruptedError:
    #     db.session.rollback()

    user_datastore.find_or_create_role(name = "User", description= 'Normal user')
    user_datastore.find_or_create_role(name = "Shop", description= 'shop')
    user_datastore.find_or_create_role(name = "Admin", description= 'admin')
    user_datastore.find_or_create_role(name = "Super_admin", description= 'super admin')

    db.session.commit()

    if not user_datastore.get_user("user@test.com"):
        user_datastore.create_user(email = "user@test.com", password = "111111")
        db.session.commit()
    if not user_datastore.get_user("shop@test.com"):
        user_datastore.create_user(email = "shop@test.com", password = "111111")

    if not user_datastore.get_user('admin@test.com'):
        user_datastore.create_user(email ="admin@test.com", password = '111111')
    #
    db.session.commit()

    user_datastore.add_role_to_user('user@test.com','User')
    user_datastore.add_role_to_user('shop@test.com','Shop')
    user_datastore.add_role_to_user('admin@test.com','Admin')
    #
    db.session.commit()
    try:
        category = {u"生物医药类":[u"生物类药物",u"疫苗",u"诊断试剂",u"医用材料",u"生物治疗"],
                    u"生物能源类":[u"生物液体燃料",u"生物质气化固体燃料"],
                    u"生物化工类":[u"生物基燃料",u"酶制剂",u"生物反应器"],
                    u"生物农业类":[u"生物育种",u"生物农药",u"生物农制品",u"食品及化妆品添加剂"],
                    u"生物环境类":[u"生物环保制品",u"污染检测",u"生物修复"]}
        for key, v in category.items():
            if Product_Category.query.filter_by(category_name = key).first() == None:
                category_patent = Product_Category(category_name=key,parent_id=0)
                db.session.add(category_patent)
                db.session.commit()
                for item in v :
                    if Product_Category.query.filter_by(category_name = item).first() == None:
                        category_child = Product_Category(category_name= item, parent_id=category_patent.id)
                        db.session.add(category_child)
                        db.session.commit()
            db.session.commit()
    except:
        db.session.rollback()
        current_app.logger.error(traceback.format_exc())
        abort(500, traceback.format_exc())





from . import user
from . import auth
from . import address
from . import product
from . import shop
from . import cart