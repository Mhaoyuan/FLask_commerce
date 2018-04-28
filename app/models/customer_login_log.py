from . import db, AppModel

class Login_Log(AppModel):
    __tablename__ = 'customer_login_log'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    login_ip = db.Column(db.String(16))
    login_type = db.Column(db.Boolean, nullable=False)