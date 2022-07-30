from flask import Blueprint, render_template,flash
from flask_login import login_required,current_user
from app.models import db

from app.models import Statia
from app.models import User
from app.user.home.forms import StatiaForm

auth_home_blueprint = Blueprint('auth_home',__name__,template_folder='templates')


@auth_home_blueprint.route('/welcome-home',methods=['GET','POST'])
@login_required
def create():

    form = StatiaForm()

    if form.validate_on_submit():


        title = form.title.data
        content = form.content.data
        user_id = current_user.id
        print(current_user)
        cont = Statia(title=title,content=content,user_id=user_id)

        db.session.add(cont)
        db.session.commit()
        flash('SUCCESS')

    return render_template('auth_home.html',form=form)


