from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.user.profile.forms import UploadPhotoForm, RemovePhotoForm,UpdateForm
from werkzeug.utils import secure_filename
from app.models import db,User,EditProfile,Statia,Likes,Comments
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
    user_data = Likes.query.filter_by(post_id=current_user.id)


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
            'content': post.content,
            'user_id': post.user_id,
            'likes':post.likes,
            'comments':post.comments,
            'created_post_date': post.created_post_date,
        })

    return render_template('profile.html',form=form,user_post=user_post,uform=uform,user_info=user_all,user_posts=user_posts,user_data=user_data)



@profile_blueprint.route('/profile-like-post/<post_id>', methods=['GET'])
@login_required
def profile_like(post_id):

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





    return redirect(url_for('profile.profile'))

