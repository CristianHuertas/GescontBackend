from typing import List
from typing import  Dict
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_conexion import obtener_sesion

from db import gestion_db
from db.gestion_db import GestionInDB
from models.gestion_model import Gestion
from db.users_db import UserInDB


router = APIRouter()


""" @router.put("/gestion/registroSave", response_model=GestionOut)#crear una nueva gestion
async def save_gestion(gestion: GestionIn, sesion: Session = Depends(obtener_sesion)):
    gestion_nueva = GestionInDB(**gestion.dict())   
    
     
    
    sesion.add(gestion_nueva)
    sesion.commit()
    sesion.refresh(gestion_nueva)

    return gestion_nueva  """

@router.post("/gestion/registroSave")#crear un nuevo cliente
async def save_gestion(gestion: Gestion, sesion: Session = Depends(obtener_sesion)):

    gestion_nuevo = GestionInDB(**gestion.dict())   
    sesion.add(gestion_nuevo)
    sesion.commit()
    sesion.refresh(gestion_nuevo)

    return gestion_nuevo     


@router.get("/gestion/registroGetAll/{id_cliente}") #mostrar todos los clientes
async def get_clientes(id_cliente: int,sesion: Session = Depends(obtener_sesion)):
    todas_gestiones= sesion.query(GestionInDB).filter_by(id_cliente=id_cliente).all().order_by(GestionInDB.id_gestion.desc())
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