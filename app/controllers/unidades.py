from models.unidad import Unidad
from db import db

class UnidadesController:

    def get_unidades(self):
        unidades = db.session.query(Unidad).all()
        unidades = [u.to_dict() for u in unidades]
        return unidades

