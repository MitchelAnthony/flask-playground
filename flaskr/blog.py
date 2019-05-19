from datetime import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr import db
from flaskr.models.user import User
from flaskr.models.blog import Blog

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    posts = Blog.query.all()

    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'
        
        if error is not None:
            flash(error)
        else:
            new_blog = Blog(
                title = title,
                body = body,
                author_id = g.user.id,
                created = datetime.now()
            )
            db.session.add(new_blog)
            db.session.commit()
            return redirect(url_for('blog.index'))
    
    return render_template('blog/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'
        
        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            db.session.commit()
            return redirect(url_for('blog.index'))
    
    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.index'))

def get_post(id, check_author=True):
    post = Blog.query.get(id)

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))
    
    if check_author and post.author_id != g.user.id:
        abort(403)
    
    return post
