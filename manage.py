import os


import sys
import click
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models.role import Role
from app.models.user import User
from app.models.customer_addr import Addr
from app.models.customer_level_inf import Level
from app.models.customer_point_log import Point_Log
from app.models.customer_balance_log import Balance_Log
from app.models.customer_login_log import Login_Log
from app.models.supplier_info import Supplier_Info
from app.models.product_category import Product_Category
from app.models.prouduct_info import Product_info
from app.models.brand_info import Brand_info
from app.models.sku_price import Sku_price
from flask_script import Manager, Shell
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
                Login_Log = Login_Log, Supplier_Info = Supplier_Info,Product_Category = Product_Category,
                Product_info = Product_info, Brand_info = Brand_info, Sku_price = Sku_price)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def db_init():
    # connection = MySQLdb.connect(host = '3306', user = 'root', passwd = '9527')
    # engine = create_engine('mysql+mysqldb://root:9527@127.0.0.1:3306/flask_e')
    # cursor = connection.cursor()
    # db.create_all()


    pass

if __name__ =='__main__':
    manager.run()