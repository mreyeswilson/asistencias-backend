from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, mapped_column
from db import db

class Localidad(db.Model):

    __tablename__ = 'localidades'

    id =  mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    tecnico = Column(String(50), nullable=True)
    estado = Column(String(50), nullable=True, default="activa")
    unidades = relationship("Unidad", back_populates="localidad")

    def __init__(self, nombre, tecnico, estado):
        self.nombre = nombre
        self.tecnico = tecnico
        self.estado = estado
        

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tecnico": self.tecnico,
            "estado": self.estado,
            "unidades": [u.to_dict() for u in self.unidades]
        }