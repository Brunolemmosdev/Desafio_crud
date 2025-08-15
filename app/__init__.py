from flask import Flask
from app.routes.funcionario_routes import bp_funcionario

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_funcionario)
    return app