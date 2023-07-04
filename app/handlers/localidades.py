from controllers.localidades import LocalidadesController
from flask import jsonify


def get_localidades_handler():
    ctrl = LocalidadesController()
    localidades = ctrl.get_localidades()
    return jsonify(localidades)

def update_localidad_handler(data):
    ctrl = LocalidadesController()
    return ctrl.update_localidad(data)
