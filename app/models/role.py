# -*- coding: utf-8 -*-
from flask_security import RoleMixin
from . import db
class Role(db.Model, RoleMixin):
    # __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default = False, index= True)
    description = db.Column(db.String(255))
    # user = db.relationship('User',backref = 'role', lazy = 'dynamic')
    def __init__(self, name,description):
        self.name = name
        self.description =description

    def __repr__(self):
        return '{}'.format(self.name)


