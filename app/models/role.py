from flask_security import RoleMixin
from . import db, user
class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default = False, index= True)
    description = db.Column(db.String(255))
    # user = db.relationship('User',backref = 'role', lazy = 'dynamic')
