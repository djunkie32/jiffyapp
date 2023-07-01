from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_share import Share
from flask_caching import Cache
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# app.secret_key ='g@bsb&048e*54jqgydxve+_0ma*(zmwov2$yzf4xc2*^l&34w$'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/jiffy'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "g@bsb&048e*54jqgydxve+_0ma*(zmwov2$yzf4xc2*^l&34w$"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# app.config["MAIL_USERNAME"] = "digitaljunkie34@gmail.com"
# app.config["MAIL_PASSWORD"] = "Entertainment@12H"
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300


db = SQLAlchemy(app)
mail = Mail(app)
share = Share(app)
cache = Cache(app)


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from . import routes
from .models import User, Url