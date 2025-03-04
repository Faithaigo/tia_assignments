import os
from flask import Flask, render_template, request, flash, redirect, url_for
from models import db,Posts, User
from forms import PostForm,RegisterForm



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


@app.route('/post/<int:post_id>')
def single_post(post_id):
    post = db.get_or_404(Posts,post_id)
    return render_template("post.html", post=post)
    

@app.route('/delete_post', methods=["DELETE"])
def delete_post():
    pass

@app.route('/edit_post', methods=["PUT"])
def edit_post():
    pass

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_user = User(full_name=form.full_name.data, email=form.email.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash("User registered successfully","success")
            return redirect(url_for("login"))
        
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET"])
def login():
    return render_template("login.html")


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)