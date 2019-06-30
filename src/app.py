from typing import Any
from flask import Flask


App = Any


def create_app() -> App:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: App) -> None:
    from .views import home
    app.register_blueprint(home)
