from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    # Registrar blueprints
    from .routes import auth, home, usuarios, niveles
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp, url_prefix='/auth')
    app.register_blueprint(usuarios.bp, url_prefix='/usuarios')

    # Configurar CORS solo para tu frontend
    CORS(app)

    return app

