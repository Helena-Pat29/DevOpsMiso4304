from flask import Flask, jsonify

from blueprints.blacklist import blacklist_blueprint
from errors.errors import ApiError
from flask_sqlalchemy import SQLAlchemy
import os
from config import Config
from models.model import db

application = app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Incluir BluePrint Utilizados
app.register_blueprint(blacklist_blueprint)

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "msg": err.description,
      #"version": os.environ["VERSION"]
    }
    return jsonify(response), err.code