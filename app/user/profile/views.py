from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.user.profile.forms import UploadPhotoForm, RemovePhotoForm,UpdateForm
from werkzeug.utils import secure_filename
from app.models import db,User
import uuid
import os


profile_blueprint = Blueprint('profile', __name__,template_folder='templates')


@profile_blueprint.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    form = UploadPhotoForm()

    user_posts = User.query.filter_by(id=current_user.id).first()
    user_post = user_posts.statia
    data = []

    if form.validate_on_submit():
        photo = form.photo.data
        photo_secure = secure_filename(photo.filename)
        pic_uid = str(uuid.uuid1()) + '_' + photo_secure
        photo = pic_uid
        form.photo.data.save(os.path.join('app/static/uploads', photo))
        current_user.photo = photo
        current_user.profile_pic = photo
        db.session.commit()
        flash('Photo uploaded successfully!')

    for post in user_post:
        data.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'user_id': post.user_id,
            'created_post_date': post.created_post_date,
        })

    return render_template('profile.html',form=form,user_post=user_post)

@login_required
def update_profile():
    form = UpdateForm()


    if form.validate_on_submit():
        name = form.name.data
        proffesion = form.proffesion.data
        skills = form.skills.data

        print(name,proffesion,skills)

    return render_template('profile.html',form=form)


