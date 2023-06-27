from controllers.localidades import LocalidadesController
from flask import jsonify


def get_localidades_handler():
    ctrl = LocalidadesController()
    localidades = ctrl.get_localidades()
    return jsonify(localidades)
