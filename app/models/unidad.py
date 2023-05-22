from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship, mapped_column
import enum
from models.localidad import Localidad
from db import db

class TipoEnum(enum.Enum):
    UPGD = "UPGD"
    UI = "UI"


class Unidad(db.Model):

    __tablename__ = 'unidades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    codigo = Column(String(50), nullable=False)
    tipo = Column(Enum(TipoEnum), nullable=False, default=TipoEnum.UPGD)
    localidad_id = mapped_column(Integer, ForeignKey('localidades.id'), nullable=False)
    localidad = relationship("Localidad", back_populates="unidades")

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
                "nombre": self.localidad.nombre
            }
        }
