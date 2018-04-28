from . import db, AppModel

class Supplier_Info(AppModel):
    __tablename__ = 'supplier_info'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    supplier_code = db.Column(db.String(8), nullable = False)
    supplier_name = db.Column(db.String(50), nullable = False)
    supplier_type = db.Column(db.Boolean, nullable= False)
    link_man = db.Column(db.String(10), nullable= False)
    phone_number = db.Column(db.String(50), nullable=False)
    bank_name = db.Column(db.String(50))
    address = db.Column(db.String(200), nullable=False)
    supplier_status = db.Column(db.Boolean, nullable=False)
    product_info = db.relationship('Product_info', backref = 'supplier', lazy = 'dynamic')

    # def __repr__(self):
        # return '<Suppier_Info % >' % self.supplier_name


