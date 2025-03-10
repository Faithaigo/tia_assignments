from flask import Blueprint,request,flash,redirect,url_for,render_template
from auth.forms import RegisterForm, LoginForm
from flask_login import login_user,logout_user
from auth.models import User
from utils import db,bcrypt

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')



@auth_blueprint.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(full_name=form.full_name.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("User registered successfully","success")
            return redirect(url_for("auth.login"))
        
    return render_template("auth/register.html", form=form)


@auth_blueprint.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        is_password = bcrypt.check_password_hash(user.password, form.password.data)
        if user and is_password:
            login_user(user)
            flash('Logged in successfully','success')
            return redirect(url_for('posts.index'))
        else:
            flash('Invalid email or password', 'error')
    return render_template("auth/login.html", form=form)

@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))