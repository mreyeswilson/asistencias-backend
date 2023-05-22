from flask import Blueprint
from handlers.unidades import get_unidades as get_unidades_handler
from migrate import migrate as migrate_handler

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/generate', methods=['POST'])
def generate():
    return 'Hello, World!'

@api.route('/sync', methods=['POST'])
def index():
    return 'Hello, World!'

@api.route('/unidades', methods=['GET'])
def get_unidades():
    return get_unidades_handler()

@api.route('/migrate', methods=['GET'])
def migrate():
    return migrate_handler()