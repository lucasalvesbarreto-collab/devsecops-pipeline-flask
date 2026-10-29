from flask import Flask

from .main import app


def create_app() -> Flask:
    return app