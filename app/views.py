from flask import render_template, request, flash

from app import app, db
from app.models import Post


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
