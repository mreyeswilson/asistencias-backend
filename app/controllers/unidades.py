from models.unidad import Unidad
from db import db
from sqlalchemy import asc

class UnidadesController:

    def get_unidades(self):
        unidades = db.session.query(Unidad).order_by(asc(Unidad.nombre)).all()
        unidades = [u.to_dict() for u in unidades]
        return unidades

    def get_unidades_x_localidad(self, id):
        unidades = db.session.query(Unidad).filter(Unidad.localidad_id == id).all()
        unidades = [u.to_dict() for u in unidades]
        return unidades
