from typing import Any
from flask import Flask


App = Any


def create_app(config_module) -> App:
    app = Flask(__name__)
    app.config.from_object(config_module)
    register_blueprints(app)
    return app


def register_blueprints(app: App) -> None:
    from .views import home
    app.register_blueprint(home)
