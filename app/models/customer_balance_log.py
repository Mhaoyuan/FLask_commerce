from . import db, AppModel

class Balance_Log(AppModel):
    __tablename__ = 'customer_balance_log'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    source = db.Column(db.SmallInteger, nullable=False) #记录来源：1 订单,2 退货单
    source_sn = db.Column(db.Integer, nullable= False)
    amount = db.Column(db.Integer,nullable=False) #变动金额

    def __repr__(self):
        return '<Balance %r>' % self.id