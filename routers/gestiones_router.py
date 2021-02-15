from typing import List
from typing import  Dict
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from db.db_conexion import obtener_sesion

from db import gestion_db
from db.gestion_db import GestionInDB
from models.gestion_model import Gestion
from db.users_db import UserInDB


router = APIRouter()




@router.post("/gestion/registroSave")#crear un nuevo cliente
async def save_gestion(gestion: Gestion, sesion: Session = Depends(obtener_sesion)):

    gestion_nuevo = GestionInDB(**gestion.dict())   
    sesion.add(gestion_nuevo)
    sesion.commit()
    sesion.refresh(gestion_nuevo)

    return gestion_nuevo     


@router.get("/gestion/registroGetAll") #mostrar todos los clientes
async def get_gestiones(id_cliente: int,sesion: Session = Depends(obtener_sesion)):
    todas_gestiones= sesion.query(GestionInDB).order_by(desc(GestionInDB.id_gestion)).filter_by(id_cliente=id_cliente).all()
    #todas_gestiones= sesion.query(GestionInDB).order_by(desc(GestionInDB.id_gestion))


    return todas_gestiones  

@router.get("/gestion/registroGetAll/{id_cliente}") #mostrar todos los clientes
async def get_gestiones(id_cliente: int,sesion: Session = Depends(obtener_sesion)):
    todas_gestiones= sesion.query(GestionInDB).order_by(desc(GestionInDB.id_gestion)).filter_by(id_cliente=id_cliente).all()
    #todas_gestiones= sesion.query(GestionInDB).order_by(desc(GestionInDB.id_gestion))


    return todas_gestiones        
    
@router.get("/gestion/registrosOrdenados") #mostrar todos los clientes
async def get_clientes(sesion: Session = Depends(obtener_sesion)):
    #todos_clientes= sesion.query(GestionInDB).order_by(GestionInDB.id_gestion.desc())
    #someselect.order_by(desc(table1.mycol))
    #todos_clientes= sesion.query(ClienteInDB).all()    
    todos_clientes= sesion.query(GestionInDB).order_by(desc(GestionInDB.id_gestion)).all()
    



    #session.query(SpreadsheetCells).order_by(SpreadsheetCells.y_index)
    
    return todos_clientes   



