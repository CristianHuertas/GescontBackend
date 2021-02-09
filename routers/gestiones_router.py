from typing import List
from typing import  Dict
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_conexion import obtener_sesion

from db import gestion_db
from db.gestion_db import GestionInDB
from models.gestion_model import Gestion


router = APIRouter()


@router.post("/gestion/registroSave")#crear una nueva gestion
async def save_gestion(gestion: Gestion, sesion: Session = Depends(obtener_sesion)):
    
    gestion_nueva = GestionInDB(**gestion.dict())   
    sesion.add(gestion_nueva)
    sesion.commit()
    sesion.refresh(gestion_nueva)

    return gestion_nueva 



@router.get("/gestion/registroGetAll") #mostrar todos los clientes
async def get_clientes(sesion: Session = Depends(obtener_sesion)):
    todas_gestiones= sesion.query(GestionInDB).all()
    return todas_gestiones   
    

""" 
@router.put("/user/transaction/", response_model=TransactionOut)
async def make_transaction(transaction_in: TransactionIn, session: Session = Depends(get_db)):
    user_in_db = session.query(UserInDB).get(transaction_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")

    if user_in_db.balance < transaction_in.value:
        raise HTTPException(status_code=400,
                            detail="No se tienen los fondos suficientes")

    user_in_db.balance = user_in_db.balance - transaction_in.value

    # Vamos a actualizar en la db
    session.commit()

    # Actualiza la sesión que tenemos creada
    session.refresh(user_in_db)

    transaction_in_db = TransactionInDB(**transaction_in.dict(), actual_balance = user_in_db.balance)

    # Como queremos agregar un nuevo valor a la bd,
    # debemos insertarle el elemento a nuestra sesión
    session.add(transaction_in_db)
    session.commit()
    session.refresh(transaction_in_db)

    return  transaction_in_db
 """