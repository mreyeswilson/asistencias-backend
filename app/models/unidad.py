import enum

from db import db
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship


class TipoEnum(enum.Enum):
    UPGD = "UPGD"
    UI = "UI"


class Unidad(db.Model):

    __tablename__ = 'unidades'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    codigo = Column(String(50), nullable=False)
    tipo = Column(Enum(TipoEnum), nullable=False, default=TipoEnum.UPGD)
    localidad_id = mapped_column(
        Integer, ForeignKey('localidades.id'), nullable=False)
    localidad = relationship("Localidad", back_populates="unidades")
    asistencias = relationship("Asistencia", back_populates="unidad")

    def __init__(self, nombre, codigo, localidad, tipo):
        self.nombre = nombre
        self.codigo = codigo
        self.localidad_id = localidad
        self.tipo = tipo

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "codigo": self.codigo,
            "tipo": self.tipo.value,
            "localidad": {
                "id": self.localidad.id,
                "nombre": self.localidad.nombre,
                "tecnico": self.localidad.tecnico,
                "estado": self.localidad.estado
            },
            "asistencias": [a.to_dict() for a in self.asistencias]
        }
