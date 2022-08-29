from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from app.models import db
from sqlalchemy import desc
from app.models import Statia
from app.models import User
from app.user.home.forms import StatiaForm

auth_home_blueprint = Blueprint('auth_home', __name__, template_folder='templates')


@auth_home_blueprint.route('/welcome-home', methods=['GET', 'POST'])
@login_required
def create():
    users = User.query.all()
    form = StatiaForm()
    data = []

    if form.validate_on_submit():

        title = form.title.data
        content = form.content.data
        user_id = current_user.id
        cont = Statia(title=title, content=content, user_id=user_id)
        print(title, content, user_id)
        db.session.add(cont)
        db.session.commit()


    for i in Statia.query.order_by(desc(Statia.id)).all():
        data.append({

            'id': i.id,
            'title': i.title,
            'content': i.content,
            'user_id': i.user_id,
            'created_post_date': i.created_post_date

        })

    return render_template('auth_home.html', form=form, data=data, users =users)

