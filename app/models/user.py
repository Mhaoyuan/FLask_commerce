from flask_security import UserMixin
from . import db, AppModel, roles_users
from flask import current_app
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
class User(AppModel,UserMixin):

    __tablename__ = 'users'
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), unique= True, index= True)
    phone = db.Column(db.Integer,unique=True, index= True)
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    roles = db.relationship('Role', secondary = roles_users,
                            backref = db.backref('users', lazy = 'dynamic'))
    password = db.Column(db.String(128))
    active = db.Column(db.Boolean)
    confirmed = db.Column(db.Boolean, default=False)
    confirmed_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    addr = db.relationship('Addr',backref = 'user', lazy = 'dynamic')
    point_log = db.relationship('Point_Log', backref = 'user', lazy = 'dynamic')
    balance_log = db.relationship('Balance_Log', backref = 'user', lazy = 'dynamic')
    login_log = db.relationship('Login_Log', backref = 'user', lazy = 'dynamic')
    supplier_info = db.relationship('Supplier_Info', backref = 'user',lazy = 'dynamic')
    order_master = db.relationship('Order_master', backref = 'user', lazy = 'dynamic')




    def __init__(self,email,active,password,roles):
        # self.phone = phone
        # self.username = username
        self.email = email
        self.active = active
        self.password = password
        self.roles =roles
    # def __repr__(self):
    #     super(User, self).__init__()
    #     if self.role is None:
    #         if self.email ==current_app.config['FLASK_ADMIN']:
    #             self.role = Role.query.filter_by(name ='admin').first()
    #         if self.role is None:
    #             self.role = Role.query.filter_by(default = True).first()

    @staticmethod
    def generate_auth_token(self, expiration = 3600):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'id':self})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user


