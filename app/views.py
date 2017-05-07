from flask import render_template, request, flash

from app import app, db
from app.models import Post
from app.pw_gen import PasswordGenerator
from app.workout_calc import WorkoutCalculator


@app.route('/')
def index():
    post_list = Post.query.all()
    return render_template('index.html',
                           post_list=post_list)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        post = Post(request.form['title'], request.form['body'])
        db.session.add(post)
        db.session.commit()
        flash('New entry was successfully posted')

    return render_template('add.html')


@app.route('/workout', methods=[GET])
def workout_calc():
    return render_template('workout.html')


@app.route('/pw_gen', methods=[GET])
def password_generator():
    return render_template('pw_gen.html')
