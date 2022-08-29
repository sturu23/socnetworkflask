from flask import Flask
from app.extensions import db, migrate,login_manager



def create_app(config_file = 'config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    migrate.init_app(app, db,render_as_batch=True)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    from app.user.views import user_blueprint
    app.register_blueprint(user_blueprint)
    from app.homepage.views import home_blueprint
    app.register_blueprint(home_blueprint)
    from app.user.profile.views import profile_blueprint
    app.register_blueprint(profile_blueprint)
    from app.user.home.views import auth_home_blueprint
    app.register_blueprint(auth_home_blueprint)


    return app

