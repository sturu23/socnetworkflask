from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user




profile_blueprint = Blueprint('profile', __name__,template_folder='templates')


@profile_blueprint.route('/profile',methods=['GET','POST'])
@login_required
def profile():

    return render_template('profile.html')




