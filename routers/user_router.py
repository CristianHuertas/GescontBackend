from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conexion import get_db
from db.users_db import UserInDB
from models.users_model import Users

""" from db.db_connection import get_db
from db.user_db import UserInDB
from db.transaction_db import TransactionInDB
from models.user_models import UserIn, UserOut
from models.transaction_models import TransactionIn, TransactionOut """

router = APIRouter()

@router.post("/user/auth/")
async def auth_user(users: Users, sesion: Session = Depends(obtener_sesion)):

    user_in_db = sesion.query(UserInDB).get(sesion.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != sesion.password:
        raise HTTPException(status_code=403, detail="Contraseña Incorrecta")

    return  {"Autenticado": True}


@router.get("/")
async def root():
    return {"message":"GesCont"}    

""" @router.get("/user/balance/{username}", response_model=UserOut)
async def get_balance(username: str, db: Session = Depends(get_db)):

    user_in_db = db.query(UserInDB).get(username)

    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")

    return  user_in_db """