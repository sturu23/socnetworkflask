from flask import Blueprint,render_template,redirect,url_for,flash,request
from app.Crud import Crud
from app.extensions import login_manager
from app.models import db
from flask_login import login_user,logout_user,login_required



from app.models import User
from app.user.forms import LoginForm,RegisterForm


user_blueprint = Blueprint('user'
                           ,__name__,
                           template_folder='templates')


@user_blueprint.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    crud = Crud()
    print('akvar')

    if form.validate_on_submit():

        username = form.name.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        secret = form.secret.data
        email2 = User.query.filter_by(email=email).first()


        if email2:
            flash('მეილი უკვე არსებობს')
            return redirect(url_for('user.register'))

        user = User(username=username,email=email,password=password,secret=secret,profile_pic='img/defaultavatar.jpg')
        db.session.add(user)
        db.session.commit()
        flash('რეგისტრაცია წარმატებით დასრულდა')


        return redirect(url_for('user.login'))
    return render_template('register.html',form=form)


@user_blueprint.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_by_email(form.email.data)

        if user is not None and user.check_password(form.password.data):
            login_user(user)

        next = request.args.get('next')

        if next is None:
            next = url_for('auth_home.create')
            flash('არასწორია შეყვანილი ინფორმაცია')
        return redirect(next)

    return render_template('login.html',form=form)


@user_blueprint.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash('თქვენ წარმატებით გამოსვლით')
    return redirect(url_for('home.home'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)