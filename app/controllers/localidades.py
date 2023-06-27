from models.localidad import Localidad
from db import db

class LocalidadesController:

    def get_localidades(self):
        localidades = db.session.query(Localidad).all()
        localidades = [u.to_dict() for u in localidades]
        return localidades