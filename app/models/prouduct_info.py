from . import db, AppModel

class Product_info(AppModel):
    __tablename__ = 'product_info'
    product_code = db.Column(db.String(16), nullable=False)
    product_name = db.Column(db.String(20), nullable=False)
    bar_code = db.Column(db.String(50))
    audit_status = db.Column(db.Boolean)
    publish_status  = db.Column(db.Boolean)
    brad_id = db.Column(db.Integer,db.ForeignKey('brand_info.id'))
    cat_id = db.Column(db.Integer,db.ForeignKey('product_category.id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier_info.id'))
    sku_price_id = db.Column(db.Integer, db.ForeignKey('sku_price.id'))