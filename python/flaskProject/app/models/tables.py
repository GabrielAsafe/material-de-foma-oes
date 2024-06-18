from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique= True)


    def __init__(self,username,password,nome,email) -> None:
        self.email = email
        self.nome = nome
        self.password = password
        self.username = username


    def __repr__(self) -> str:
        return "<User %r>" % self.username
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys= user_id)

    def __init__(self,content,user_id) -> None:
        self.content = content
        self.user_id = user_id

    def __repr__(self) -> str:
        return "<Post %r>" % self.id
    

class Folloq(db.Model):
    __tablename__ = 'follow'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id= db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('Users', foreign_keys= user_id)
    follower = db.relationship('Users', foreign_keys= follower_id)