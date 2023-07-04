import datetime as dt

from db import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship


class Asistencia(db.Model):

    __tablename__ = 'asistencias'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    fecha_asistencia = Column(DateTime, nullable=False)
    fecha_prealistamiento = Column(DateTime)
    estado = Column(String(50), nullable=False, default='Pendiente')
    epidemiologo = Column(String(50), nullable=False)

    unidad_id = mapped_column(
        Integer, ForeignKey('unidades.id'), nullable=False)
    unidad = relationship("Unidad", back_populates="asistencias")

    prealistamiento_id = mapped_column(
        Integer, ForeignKey('prealistamientos.id'), nullable=False)
    prealistamiento = relationship(
        "Prealistamiento", back_populates="asistencias")

    def to_dict(self):
        return {
            "id": self.id,
            "fecha_asistencia": self.fecha_asistencia,
            "fecha_prealistamiento": self.fecha_prealistamiento,
            "estado": self.estado,
            "epidemiologo": self.epidemiologo,
            "prealistamiento": {
                "id": self.prealistamiento.id,
                "nombre": self.prealistamiento.nombre,
                "fecha_prealistamiento": self.prealistamiento.fecha_prealistamiento,
                "archivo_zip": self.prealistamiento.archivo_zip
            },
            # "unidad": {
            #     "id": self.unidad.id,
            #     "nombre": self.unidad.nombre
            # }
        }
