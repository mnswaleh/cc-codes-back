from manage import db


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    nice_name = db.Column(db.String(128), nullable=True)
    iso = db.Column(db.String(4))
    iso_3 = db.Column(db.String(4))
    code = db.Column(db.Integer(), nullable=True)
    phone_code = db.Column(db.Integer(), nullable=True)

    def __repr__(self):
        return self.name
