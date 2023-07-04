from models.localidad import Localidad
from db import db

class LocalidadesController:

    def get_localidades(self):
        localidades = db.session.query(Localidad).all()
        localidades = [u.to_dict() for u in localidades]
        return localidades
    
    def update_localidad(self, data):
        localidad = db.session.query(Localidad).filter_by(id=data["id"]).first()
        if not localidad:
            return "No existe la localidad", 404
        localidad.nombre = data["nombre"]
        localidad.tecnico = data["tecnico"]
        localidad.estado = data["estado"]
        # db.session.add(localidad)
        db.session.commit()
        return "Localidad actualizada", 200