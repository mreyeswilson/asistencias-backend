from db import db
from flask import request, jsonify
from models.asistencia import Asistencia
from extensions import socketio
import json


def get_asistencias_x_estado():
    status = request.args.get("status")
    if status is None:
        return jsonify({"message": "No se especificó el estado"}), 400
    
    # query with like
    asistencias = db.session.query(Asistencia).filter(Asistencia.estado.like(f"%{status}%")).all()
    asistencias = [a.to_dict() for a in asistencias]
    return jsonify(asistencias)