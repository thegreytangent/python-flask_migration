from config import db

class Post(db.Model):
    id      = db.Column(db.Integer,primary_key=True)
    title   = db.Column(db.String(50))
    content = db.Column(db.String(255))


    def __repr__(self):
        return f'<Post title={self.id}, content={self.content}'

