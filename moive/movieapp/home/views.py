from . import home
from flask import render_template, redirect, url_for


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/animation/')
def animation():
    return render_template('home/animation.html')


@home.route('/movie_search/')
def movie_search():
    return render_template('home/movie_search.html')


@home.route('/movie_play/')
def movie_play():
    return render_template('home/movie_play.html')


@home.route('/login/')
def login():
    return render_template('home/login.html')


@home.route('/logout/')
def logout():
    return redirect(url_for('home.login'))


@home.route('/regist/')
def regist():
    return render_template('home/regist.html')


@home.route('/user/')
def user():
    return render_template('home/user.html')


@home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')


@home.route('/comm/')
def comm():
    return render_template('home/comm.html')


@home.route('/coll/')
def coll():
    return render_template('home/coll.html')


@home.route('/login_log/')
def login_log():
    return render_template('home/login_log.html')
