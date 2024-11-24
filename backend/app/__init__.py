from flask import Flask
from .models import db
from .api import api_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sporty.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Register the Blueprint
    app.register_blueprint(api_bp, url_prefix='/')

    return app