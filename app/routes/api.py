from flask import Blueprint
from handlers.unidades import get_unidades as get_unidades_handler
from handlers.localidades import get_localidades_handler
from migrate import migrate as migrate_handler

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/unidades', methods=['GET'])
def get_unidades():
    return get_unidades_handler()

@api.route('/unidades/<id>', methods=['GET'])
def get_unidades_x_localidad(id):
    return get_unidades_handler(id)

@api.route('/localidades', methods=['GET'])
def get_localidades():
    return get_localidades_handler()

@api.route('/migrate', methods=['GET'])
def migrate():
    return migrate_handler()