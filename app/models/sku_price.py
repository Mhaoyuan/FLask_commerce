from . import db, AppModel

class Sku_price(AppModel):
    __tablename__ = 'sku_price'
    mass = db.Column(db.String(16))
    purer = db.Column(db.String(16))
    price = db.Column(db.Integer)
    product_info = db.relationship('Product_info', backref = 'sku_price', lazy = 'dynamic')

