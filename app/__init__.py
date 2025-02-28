from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    db.init_app(app)
    migrate.init_app(app, db)

    # import routes
    from .routes import planet_bp
    from .routes import moon_bp

    # register blueprint
    app.register_blueprint(planet_bp)
    app.register_blueprint(moon_bp)

    from app.models.planet import Planet
    from app.models.moon import Moon

    # from app.models.moon import Moon

    return app

