from typing import List
from typing import  Dict
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_conexion import obtener_sesion

from db import users_db
from db.users_db import UserInDB
from models.users_model import Users

router = APIRouter()






@router.get("/user/auth") #bucar  un usuario
async def get_users(username: str, sesion: Session = Depends(obtener_sesion)):
    usuario_indb= sesion.query(UserInDB).get(username)
    return usuario_indb 


@router.get("/user/auth/{username}") #bucar  un usuario
async def get_users(username: str, sesion: Session = Depends(obtener_sesion)):
    usuario_indb= sesion.query(UserInDB).get(username)
    return usuario_indb 




""" @router.post("/user/auth/")
async def auth_user(users: Users, sesion: Session = Depends(obtener_sesion)):

    user_in_db = sesion.query(UserInDB).get(users.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != users.password:
        raise HTTPException(status_code=403, detail="Contraseña Incorrecta")

    return  {"Autenticado": True} """



""" @router.get("/user/balance/{username}", response_model=UserOut)
async def get_balance(username: str, db: Session = Depends(get_db)):

    user_in_db = db.query(UserInDB).get(username)

    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")

    return  user_in_db """