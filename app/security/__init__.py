# -*- coding: utf-8 -*-
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security import user_registered
# from app.models import db
# from manage import app
from app import user_datastore
from app.models.role import Role
from app.models.user import User
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
#
security = Security(datastore=user_datastore)

# @user_registered.connect_via(app)
# def user_registered_sighandler(app, user, confirm_token):
#     default_role = user_datastore.find_role("Pending")
#     user_datastore.add_role_to_user(user, default_role)
#     db.session.commit()