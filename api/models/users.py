from manage import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    first_name = db.Column(db.String(128))
    second_name = db.Column(db.String(128))
    password = db.Column(db.Text)

    def __repr__(self):
        return self.email
