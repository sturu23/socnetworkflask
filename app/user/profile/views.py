from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.user.profile.forms import UploadPhotoForm, RemovePhotoForm,UpdateForm
from werkzeug.utils import secure_filename
from app.models import db,User,EditProfile
import uuid
import os


profile_blueprint = Blueprint('profile', __name__,template_folder='templates')


@profile_blueprint.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    #forms
    form = UploadPhotoForm()
    uform = UpdateForm()
    #forms

    #querys
    user_posts = User.query.filter_by(id=current_user.id).first()
    user_post = user_posts.statia

    user_all = EditProfile.query.filter_by(id=current_user.id).first()




    #querys
    data = []

    if form.submit2.data and form.validate():
        #for picture upload

        photo = form.photo.data
        photo_secure = secure_filename(photo.filename)
        pic_uid = str(uuid.uuid1()) + '_' + photo_secure
        photo = pic_uid
        form.photo.data.save(os.path.join('app/static/uploads', photo))
        current_user.photo = photo
        current_user.profile_pic = photo
        db.session.commit()
        flash('Photo uploaded successfully!')

    if uform.submit1.data and uform.validate():

        #for profile update
        username = uform.username.data
        proffesion = uform.proffesion.data
        skills = uform.skills.data
        splited_skills = skills.split(',')


        user = EditProfile.query.filter_by(id=current_user.id).first()
        if user:
            user.username = username
            user.proffesion = proffesion
            user.skills = skills
            user.id = current_user.id
            db.session.commit()
        else:
            db_edit = EditProfile(username=username,proffesion=proffesion,skills=skills,user_id=current_user.id)
            db.session.add(db_edit)
            db.session.commit()




    for post in user_post:
        data.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'user_id': post.user_id,
            'created_post_date': post.created_post_date,
        })

    return render_template('profile.html',form=form,user_post=user_post,uform=uform,user_info=user_all)





