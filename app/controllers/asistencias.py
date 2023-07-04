from db import db
from datetime import datetime
from models.asistencia import Asistencia as AsistenciaModel
from extensions import socketio
from flask_socketio import emit

class Asistencia:

    def check_expired_asistencias(self):
        asistencias = db.session.query(AsistenciaModel).filter(AsistenciaModel.estado.like(f"%pendiente%")).all()
        for asistencia in asistencias:
            if asistencia.fecha_prealistamiento < datetime.now():
                asistencia.estado = "vencida"
                db.session.add(asistencia)
        db.session.commit()
        if len(asistencias) > 0:
            print("Asistencias vencidas actualizadas")
            socketio.emit("asistencias", {"msg": "Asistencias vencidas actualizadas"})


asistencia = Asistencia()