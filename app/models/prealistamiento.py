from db import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, mapped_column

class Prealistamiento(db.Model):

    __tablename__ = 'prealistamientos'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    fecha_prealistamiento = Column(DateTime, nullable=False)
    archivo_zip = Column(String(50), nullable=True)
    asistencias = relationship("Asistencia", back_populates="prealistamiento", cascade="all, delete-orphan")

    def __init__(self, nombre, fecha_prealistamiento, archivo_zip):
        self.nombre = nombre
        self.fecha_prealistamiento = fecha_prealistamiento
        self.archivo_zip = archivo_zip


    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha_prealistamiento": self.fecha_prealistamiento,
            "archivo_zip": self.archivo_zip,
            "asistencias": [asistencia.to_dict() for asistencia in self.asistencias]
        }
