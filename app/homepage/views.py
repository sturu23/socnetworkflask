from flask import Blueprint, render_template, redirect, url_for, flash, request



home_blueprint = Blueprint('home',
                           __name__
                           ,template_folder='templates')


@home_blueprint.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')