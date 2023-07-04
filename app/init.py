from dotenv import load_dotenv
load_dotenv()

from db import db
from flask import Flask
from flask_cors import CORS
from routes.api import api
import multiprocessing
from scheduling.main import run
from extensions import socketio
import logging

app = Flask(__name__)

CORS(app)

socketio.init_app(app)

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.WARNING)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()
db.init_app(app)
db.create_all()


app.register_blueprint(api)

# process = multiprocessing.Process(target=run, name="Cronjobs")

if __name__ == '__main__':

    # process.start()
    socketio.run(app, host="0.0.0.0", port=5001, allow_unsafe_werkzeug=True)
    # process.terminate()

