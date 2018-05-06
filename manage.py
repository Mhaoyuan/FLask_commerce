# -*- coding: utf-8 -*-
import os


import sys
import click
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Server
from flask_security import user_registered
from app import user_datastore
from app import create_app, db
from app.models.role import Role
from app.models.user import User
from app.models.customer_addr import Addr
from app.models.customer_level_inf import Level
from app.models.customer_point_log import Point_Log
from app.models.customer_balance_log import Balance_Log
from app.models.customer_login_log import Login_Log
from app.models.shop_info import Shop_Info
from app.models.product_category import Product_Category
from app.models.prouduct_info import Product_info
from app.models.brand_info import Brand_info
from app.models.sku_price import Sku_price
from app.models.order_master import Order_master
from flask_security import Security,SQLAlchemyUserDatastore
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# engine = create_engine('mysql+mysqldb://root:9527@127.0.0.1/flask_e',
#                        convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()
manager = Manager(app)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app= app, db=db, User=User, Role=Role, Addr = Addr,
                Level = Level,Point_Log = Point_Log, Balance_Log = Balance_Log,
                Login_Log = Login_Log, Shop_Info = Shop_Info,Product_Category = Product_Category,
                Product_info = Product_info, Brand_info = Brand_info, Sku_price = Sku_price,
                Order_master = Order_master)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host ='0.0.0.0'))

@manager.command
def db_init():
    # connection = MySQLdb.connect(host = '3306', user = 'root', passwd = 'demo')
    # engine = create_engine('mysql+mysqldb://root:demo@flasksql/db')
    # cursor = connection.cursor()
    db.drop_all()
    db.create_all()

# def user_registered_sighandler(user,app):
#     default_role = user_datastore.find_role("Pending")
#     user_datastore.add_role_to_user(user, default_role)
#     db.session.commit()
#
# user_registered.connect(user_registered_sighandler)

@user_registered.connect_via(app)
def user_registered_sighandler(app, user, confirm_token):
    default_role = user_datastore.find_role("User")
    user_datastore.add_role_to_user(user, default_role)
    db.session.commit()

if __name__ =='__main__':
    manager.run()