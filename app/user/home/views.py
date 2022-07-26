from flask import Blueprint, render_template
from flask_login import login_required

from app.user.home.forms import StatiaForm

auth_home_blueprint = Blueprint('auth_home',__name__,template_folder='templates')


@auth_home_blueprint.route('/welcome-home',methods=['GET','POST'])
@login_required
def create():

    form = StatiaForm()

    if form.validate_on_submit():
        title= form.title.data
        content = form.statia.data

        print(title,content)

    return render_template('auth_home.html',form=form)


