from . import db,AppModel
class Order_master(AppModel):
    __tablename__ = 'order_master'
    order_sn = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    addr_id = db.Column(db.Integer, db.ForeignKey('customer_addr.id'))
