from flask_security import Security, SQLAlchemyUserDatastore

from app.models import db
from app.models.role import Role
from app.models.user import User
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
#
# security = Security(datastore=user_datastore)