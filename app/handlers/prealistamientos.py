from flask import jsonify, request, send_from_directory
from controllers.prealistamientos import prealistamiento
from models.prealistamiento import Prealistamiento
import uuid
from db import db
import os
import shutil
from enums import MONTHS


def generatePrealistamientosHandler():
    file = request.files["file"]
    original_filename = file.filename.split(".")[0]
    ext = file.filename.split(".")[-1]
    filename = f"{str(uuid.uuid4())}.{ext}"


    with open(f"tmp/{filename}", "wb") as f:
        f.write(file.read())

    result = prealistamiento.generar(filename, original_filename)

    if result:
        return jsonify({"message": f"Las siguientes unidades no fueron procesadas: \n{', '.join(result)}"}), 400
    
    return "Prealistamientos generados exitosamente", 200

def get_prealistamientos_handler():
    prealistamientos = db.session.query(Prealistamiento).all()
    return [prealistamiento.to_dict() for prealistamiento in prealistamientos]

def delete_preenlistment_handler(id):
    prealistamiento = db.session.query(Prealistamiento).filter_by(id=id).first()
    name = prealistamiento.nombre
    month = MONTHS[prealistamiento.fecha_prealistamiento.strftime("%B")]
    db.session.delete(prealistamiento)
    db.session.commit()

    path = f"storage/{month}/{name}"
    if os.path.exists(path):
        shutil.rmtree(path)

    return "Prealistamiento eliminado exitosamente", 200
