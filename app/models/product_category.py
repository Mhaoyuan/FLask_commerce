from . import db, AppModel

class Product_Category(AppModel):
    __tablename__ = 'product_category'
    category_name = db.Column(db.String(10),nullable=False)
    # category_code = db.Column(db.String(10),nullable=False)
    parent_id = db.Column(db.SmallInteger)
    category_level = db.Column(db.SmallInteger)
    category_status = db.Column(db.SmallInteger)
    product_info = db.relationship('Product_info', backref = 'category',lazy = 'dynamic')
    def __repr__(self):
        return '<Product_CateGory %r>' % self.category_name