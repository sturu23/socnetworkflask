from flask import Blueprint,render_template,redirect,url_for,flash,request
from flask_login import login_required

auth_home_blueprint = Blueprint('auth_home',__name__,template_folder='templates')


@auth_home_blueprint.route('/welcome-home',methods=['GET','POST'])
@login_required
def ahome():

    return render_template('auth_home.html')