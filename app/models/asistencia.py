from db import db
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, mapped_column

class Asistencia(db.Model):
    
    __tablename__ = 'asistencias'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    fecha_asistencia = Column(DateTime, nullable=False)
    fecha_prealistamiento = Column(DateTime)
    estado = Column(String(50), nullable=False, default='Pendiente')
