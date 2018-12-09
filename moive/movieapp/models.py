from flask import Flask
from datetime import datetime
import pymysql

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:19940705@127.0.0.1:3306/moviea"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String(99), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    pwd = db.Column(db.String(99))
    email = db.Column(db.String(99), unique=True)
    phone = db.Column(db.String(11), unique=True)
    intro = db.Column(db.Text)
    face = db.Column(db.String(199), unique=True)
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    uid = db.Column(db.String(199), unique=True)  # 唯一标志符号
    user_logs = db.relationship('User_log', backref='user')
    comms = db.relationship('Comm', backref='user')
    colls = db.relationship('Coll', backref='user')

    def __repr__(self):
        return "<User %r>" % self.name


class User_log(db.Model):
    __tablename__ = 'user_log'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(99))
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<User_log %r>" % self.id


class Label(db.Model):
    __tablename__ = 'label'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), unique=True)
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    movies = db.relationship('Movie', backref='label')

    def __repr__(self):
        return "<Label %r>" % self.name


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(199), unique=True)
    url = db.Column(db.String(199), unique=True)
    intro = db.Column(db.Text)
    logo = db.Column(db.String(199), unique=True)
    star = db.Column(db.SmallInteger)
    show_time = db.Column(db.Date)
    length = db.Column(db.String(99))
    play_num = db.Column(db.BigInteger)
    comm_num = db.Column(db.BigInteger)
    label_id = db.Column(db.Integer, db.ForeignKey('label.id'))
    place = db.Column(db.String(199))
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    comms = db.relationship('Comm', backref='movie')
    colls = db.relationship('Coll', backref='movie')

    def __repr__(self):
        return "<Movie %r>" % self.title


class Preview(db.Model):
    __tablename__ = 'preview'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(199), unique=True)
    logo = db.Column(db.String(199), unique=True)
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Preview %r>" % self.title


class Comm(db.Model):
    __tablename__ = 'comm'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Comm %r>" % self.id


class Coll(db.Model):
    __tablename__ = 'coll'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Coll %r>" % self.id


class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(99), unique=True)
    url = db.Column(db.String(199), unique=True)

    def __repr__(self):
        return "<Auth %r>" % self.name


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(99), unique=True)
    auths = db.Column(db.String(399))
    admins = db.relationship('Admin', backref='role')

    def __repr__(self):
        return "<Role %r>" % self.name


# ///////////////////管理员

class Admin(db.Model):
    __tablename__ = 'admin'
    name = db.Column(db.String(99), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    pwd = db.Column(db.String(99))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    admin_logs = db.relationship('Admin_log', backref='admin')
    Ope_log = db.relationship('Ope_log', backref='admin')

    def __repr__(self):
        return "<Admin %r>" % self.name


class Admin_log(db.Model):
    __tablename__ = 'admin_log'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(99))
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Admin_log %r>" % self.id


class Ope_log(db.Model):
    __tablename__ = 'ope_log'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(99))
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Ope_log %r>" % self.id


# if __name__ == "__main":
#     # db.create_all()
#     role = Role(
#         name="haola"
#     )
#     db.session.add(role)
#     db.session.commit()
