from app import db
from werkzeug.security import  generate_password_hash,check_password_hash
from flask_login import UserMixin, login_manager
from sqlalchemy.orm import relationship
from datetime import datetime

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    secret = db.Column(db.String(128))
    profile_pic = db.Column(db.String(20), nullable=True)
    account_created_time = db.Column(db.DateTime,default=datetime.utcnow)
    likes = db.relationship('Likes',backref='user',passive_deletes=True)
    comments = db.relationship('Comments',backref='user',passive_deletes=True)

    def __init__(self, username, email, password,secret,profile_pic,likes,comments):
        self.profile_pic = profile_pic
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.secret = secret
        self.likes = likes
        self.comments = comments


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


    @classmethod
    def find_by_email(cls, email):
        email = cls.query.filter_by(email=email).first()
        if email:
            return email


class Statia(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('statia', lazy=True))
    post_pic = db.Column(db.String(20),nullable=True)
    created_post_date = db.Column(db.DateTime(timezone=True),default=datetime.now())
    user_img = db.relationship('User', backref='user')
    likes = db.relationship('Likes', backref='statia', passive_deletes=True)
    comments = db.relationship('Comments', backref='statia',uselist=False, passive_deletes=True)

    def __init__(self, title, content,user_id,likes,comments):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.likes = likes
        self.comments = comments



    @classmethod
    def find_statia_by_id(cls,id):
        return cls.query.filter_by(id=id).first()


class EditProfile(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key= True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    username = db.Column(db.String(50))
    proffesion = db.Column(db.String(50))
    skills = db.Column(db.String(20))


    def __init__(self,user_id,username,proffesion,skills):
        self.user_id = user_id
        self.username = username
        self.proffesion = proffesion
        self.skills = skills

class Likes(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete="CASCADE"),nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey('statia.id',ondelete="CASCADE"),nullable=False)

class Comments(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    text = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.now())
    post_id = db.Column(db.Integer, db.ForeignKey('statia.id', ondelete="CASCADE"), nullable=False)

    # def __init__(self,text,date_created,user_id,post_id):
    #     self.post_id = post_id
    #     self.user_id = user_id
    #     self.text = text
