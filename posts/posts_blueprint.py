from flask import Blueprint, render_template, redirect, request, url_for,flash
from flask_login import  login_required
from posts.forms import PostForm
from posts.models import Posts
from utils import db


posts_blueprint = Blueprint('posts',__name__, template_folder='templates')

def fetch_all_posts():
    all_posts = db.session.execute(db.select(Posts)).scalars()
    return all_posts


@posts_blueprint.route('/')
def index():
    all_posts = fetch_all_posts()
    return render_template('posts/index.html', posts=all_posts)


@posts_blueprint.route('/list')
@login_required
def posts():
    all_posts = fetch_all_posts()
    return render_template("posts/posts.html", posts=all_posts)

@posts_blueprint.route('/new_post', methods=["POST","GET"])
@login_required
def new_post():
    form = PostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_post = Posts(title=form.title.data, content=form.content.data, author=form.author.data)
            db.session.add(new_post)
            db.session.commit()
            flash("Post added successfully","success")
            return redirect(url_for("posts.index"))
    return render_template("posts/new_post.html", form=form)


@posts_blueprint.route('/post/<int:post_id>')
@login_required
def single_post(post_id):
    post = db.get_or_404(Posts,post_id)
    return render_template("posts/post.html", post=post)
    

@posts_blueprint.route('/delete_post', methods=["DELETE"])
def delete_post():
    pass

@posts_blueprint.route('/edit_post', methods=["PUT"])
def edit_post():
    pass