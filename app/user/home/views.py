from flask import Blueprint, render_template, flash,redirect,url_for
from flask_login import login_required, current_user
from app.models import db
from sqlalchemy import desc
from app.models import Statia
from app.models import User,Likes
from app.user.home.forms import StatiaForm

auth_home_blueprint = Blueprint('auth_home', __name__, template_folder='templates')


@auth_home_blueprint.route('/welcome-home', methods=['GET', 'POST'])
@login_required
def create():
    users = User.query.all()
    form = StatiaForm()
    data = []
    post = Statia.query.all()



    # p = Statia.query.filter_by(id=i)
    # print(p)

    user_pic = Statia.query.all()

    for pic in user_pic:
        print(pic.user.profile_pic)




    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id = current_user.id
        cont = Statia(title=title, content=content, user_id=user_id)
        db.session.add(cont)
        db.session.commit()


    for i in Statia.query.order_by(desc(Statia.id)).all():
        data.append({

            'id': i.id,
            'content': i.content,
            'user_id': i.user_id,
            'user_img': i.user.profile_pic,
            'created_post_date': i.created_post_date,

        })





    return render_template('auth_home.html', form=form, data=data, users=users, post=post,user_pic=user_pic)


@auth_home_blueprint.route('/like-post/<post_id>', methods=['GET'])
@login_required
def like(post_id):
    user = User.query.all()
    post = Statia.query.filter_by(id=post_id)
    like = Likes.query.filter_by(user_id=current_user.id,post_id=post_id).first()

    if not post:
        flash('Post does not exist')

    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        likes = Likes(user_id = current_user.id,post_id=post_id)
        db.session.add(likes)
        db.session.commit()


    return redirect(url_for('auth_home.create'))
