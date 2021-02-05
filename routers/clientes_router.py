from typing import List
from typing import  Dict
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_conexion import obtener_sesion
from db import cliente_db
from db.cliente_db import ClienteInDB
from models.cliente_model import Cliente

router = APIRouter()

@router.get("/cliente/registroGetAll") #mostrar todos los clientes
async def get_clientes(sesion: Session = Depends(obtener_sesion)):
    todos_clientes= sesion.query(ClienteInDB).all()
    return todos_clientes    

    

@router.get("/cliente/registroGet") #consultar un solo cliente por id_cliente
async def get_cliente (id_cliente: int, sesion: Session = Depends(obtener_sesion)):
    este_cliente= sesion.query(ClienteInDB).get(id_cliente)

    if este_cliente==None:
        raise HTTPException(status_code=404, detail=" El cliente no existe ")
    
    return este_cliente 

#revisar por que no lo veo claro
@router.get("/cliente/registroGet/{id_cliente}") #consultar un solo cliente por id_cliente cuando viene de la url
async def get_cliente(id_cliente:int, sesion: Session = Depends(id_cliente)):
    este_cliente= sesion.query(ClienteInDB).get(id_cliente)
    if este_cliente==None:
        raise HTTPException(status_code=404, detail=" El cliente no existe ")
    return este_cliente    


@router.get("/")
async def root():
    return {"message":"GesCont"} 

""" ///////////////////////////// """
@router.put("/cliente/registroPut") #cambiar datos de un cliente
async def update_cliente(cliente: Cliente, sesion: Session = Depends(obtener_sesion)):
    cliente_in_db=sesion.query(ClienteInDB).get(cliente.id_cliente)

    if cliente_in_db == None:
        raise HTTPException(status_code=404,
                            detail=" El cliente no existe ")
    
    cliente_in_db.id_cliente= cliente.id_cliente
    cliente_in_db.documento= cliente.documento
    cliente_in_db.razon_social= cliente.razon_social
    cliente_in_db.contacto= cliente.contacto
    cliente_in_db.telefono= cliente.telefono
    cliente_in_db.ciudad= cliente.ciudad
    cliente_in_db.correo= cliente.correo
    cliente_in_db.detalle= cliente.detalle

    # Vamos a actualizar en la db
    sesion.commit()

    # Actualiza la sesión que tenemos creada
    sesion.refresh(cliente_in_db)
    
    return  cliente_in_db

@router.post("/cliente/registroSave")#crear un nuevo cliente
async def save_cliente(cliente: Cliente, sesion: Session = Depends(obtener_sesion)):
    busca_cliente= sesion.query(ClienteInDB).get(cliente.id_cliente)
    if busca_cliente != None:
        raise HTTPException(status_code=404,
                            detail=" El cliente ya existe ")
    cliente_nuevo = ClienteInDB(**cliente.dict())   
    sesion.add(cliente_nuevo)
    sesion.commit()
    sesion.refresh(cliente_nuevo)

    return cliente_nuevo 


@router.delete("/cliente/registroDel/{id_cliente}") # Elimina un cliente por id_cliente
def delete_cliente(id_cliente:int, sesion: Session = Depends(obtener_sesion)):
    cliente_eliminado= sesion.query(ClienteInDB).get(id_cliente)

    if cliente_eliminado==None:
        raise HTTPException(status_code=404, detail=" El cliente no existe ")

    sesion.delete(cliente_eliminado)
    sesion.commit()
    

    return id_cliente

