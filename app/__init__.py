from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    # import routes
    from .routes import planet_bp

    # register blueprint
    app.register_blueprint(planet_bp)

    return app

