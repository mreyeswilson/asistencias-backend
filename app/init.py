from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from routes.api import api
from db import db

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()
db.init_app(app)
db.create_all()


app.register_blueprint(api)

if __name__ == '__main__':
    app.run(port=5001, debug=True)