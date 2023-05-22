from controllers.unidades import UnidadesController 
from flask import jsonify

def get_unidades():
    ctrl = UnidadesController()
    unidades = ctrl.get_unidades()
    return jsonify(unidades)
