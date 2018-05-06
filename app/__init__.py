# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension
from config import config
from app.admin import admin
from flask_security import SQLAlchemyUserDatastore,Security
from .models import db,User,Role
from flask_admin import Admin


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
toolbar =DebugToolbarExtension()
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    # user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app,datastore= user_datastore)
    db.init_app(app)
    admin.init_app(app)
    # security.init_app(app)
    # toolbar.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix = '/api/v1')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    return app
