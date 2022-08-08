from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.user.profile.forms import UploadPhotoForm, RemovePhotoForm
from werkzeug.utils import secure_filename
from app.models import db,User
import uuid
import os


profile_blueprint = Blueprint('profile', __name__,template_folder='templates')


@profile_blueprint.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    form = UploadPhotoForm()

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



    return render_template('profile.html',form=form)




