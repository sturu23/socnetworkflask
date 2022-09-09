from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager,logout_user,login_required

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
login_manager = LoginManager()
