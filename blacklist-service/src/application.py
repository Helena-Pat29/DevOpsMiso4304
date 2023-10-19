from dotenv import load_dotenv
loaded = load_dotenv('.env.development')


from flask import Flask, jsonify

from .blueprints.blacklist import blacklist_blueprint
from .errors.errors import ApiError
from flask_sqlalchemy import SQLAlchemy
import os
from .models.model import db

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/blacklist_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}")
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@0.0.0.0:5432/users'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

#Incluir BluePrint Utilizados
application.register_blueprint(blacklist_blueprint)

app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    application.run(port = 5000, debug = True)
    
@application.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "msg": err.description,
      #"version": os.environ["VERSION"]
    }
    return jsonify(response), err.code