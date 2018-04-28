from . import db,AppModel

class Level(AppModel):
    __tablename__ = 'customer_level_inf'
    level_name = db.Column(db.String(10), nullable=False)
    min_point = db.Column(db.Integer, nullable=False)
    max_point = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Level %r>' % self.level_name

