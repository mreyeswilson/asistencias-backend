from controllers.unidades import UnidadesController 
from flask import jsonify

def get_unidades(id=None):
    ctrl = UnidadesController()
    if id:
        unidades = ctrl.get_unidades_x_localidad(id)
    else:
        unidades = ctrl.get_unidades()
    return jsonify(unidades)
