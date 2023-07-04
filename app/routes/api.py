from flask import Blueprint, request
from handlers.asistencias import get_asistencias_x_estado
from handlers.localidades import (get_localidades_handler,
                                  update_localidad_handler)
from handlers.prealistamientos import (delete_preenlistment_handler,
                                       generatePrealistamientosHandler,
                                       get_prealistamientos_handler)
from handlers.unidades import get_unidades as get_unidades_handler
from migrate import migrate as migrate_handler

from handlers.auth import login_handler, check_users_handler, register_user_handler

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

@api.route('/localidad', methods=['PUT'])
def update_localidad():
    data = request.get_json()
    return update_localidad_handler(data)

@api.route('/migrate', methods=['GET'])
def migrate():
    return migrate_handler()


@api.route("/pre-enlistments", methods=["POST"])
def preenlistments():
    return generatePrealistamientosHandler()

@api.route("/pre-enlistments", methods=["GET"])
def get_preenlistments():
    return get_prealistamientos_handler()

@api.route("/pre-enlistments/<id>", methods=["DELETE"])
def delete_preenlistment(id):
    return delete_preenlistment_handler(id)

@api.route("/asistencias", methods=["GET"])
def asistencias():
    return get_asistencias_x_estado()


@api.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return login_handler(data)

@api.route("/users/check", methods=["GET"])
def check_users():
    return {
        "users": check_users_handler()
    }

@api.route("/users/register", methods=["POST"])
def register_user():
    data = request.get_json()
    return register_user_handler(data)