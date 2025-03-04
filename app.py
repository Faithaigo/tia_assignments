import os
from flask import Flask, render_template, request, flash, redirect, url_for
from models import db,Posts
from forms import PostForm



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = os.getenv("CSRF_KEY")


db.init_app(app)


def fetch_all_posts():
    posts = db.session.execute(db.select(Posts)).scalars()
    return posts


@app.route('/')
def index():
    posts = fetch_all_posts()
    return render_template("index.html", posts=posts)


@app.route('/posts')
def posts():
    posts = fetch_all_posts()
    return render_template("posts.html", posts=posts)

@app.route('/new_post', methods=["POST","GET"])
def new_post():
    form = PostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_post = Posts(title=form.title.data, content=form.content.data, author=form.author.data)
            db.session.add(new_post)
            db.session.commit()
            flash("Post added successfully","success")
            return redirect(url_for("index"))
    return render_template("new_post.html", form=form)

@app.route('/delete_post', methods=["PUT"])
def delete_post():
    pass

@app.route('/edit_post', methods=["DELETE"])
def edit_post():
    pass

@app.route('/register', methods=["GET"])
def register():
    return render_template("register.html")


@app.route('/login', methods=["GET"])
def login():
    return render_template("login.html")


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)