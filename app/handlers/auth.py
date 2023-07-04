import os
from datetime import datetime, timedelta

import bcrypt
import jwt
from db import db
from models.usuario import Usuario
import json


def login_handler(data):
    usuario = db.session.query(Usuario).filter_by(
        username=data["username"]).first()
    if usuario:
        if bcrypt.checkpw(data["password"].encode("utf-8"), usuario.password.encode("utf-8")):
            token = jwt.encode({
                "user": usuario.to_dict(),
                "exp": datetime.utcnow() + timedelta(hours=1)
            }, os.environ["JWT_SECRET"], algorithm="HS256")
            
            return token, 200
        else:
            return {"message": "Contraseña incorrecta"}, 401
    else:
        return {"message": "Usuario no registrado"}, 401


def check_users_handler():
    usuarios = db.session.query(Usuario).all()
    return len(usuarios) > 0


def register_user_handler(data):
    usuario = Usuario(
        username=data["username"],
        password=bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
        nombre=data["nombre"],
        apellido=data["apellido"],
        email=data["email"],
    )
    db.session.add(usuario)
    db.session.commit()

    return "Usuario registrado exitosamente", 200
