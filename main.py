""" from db import cliente_db """
from db.cliente_db import ClienteInDB
from db.users_db import UserInDB

from models.cliente_model import Cliente
from models.users_model import Users

from datetime import date
from typing import  Dict
from fastapi import FastAPI, HTTPException

from routers.clientes_router       import router as router_clientes
from routers.user_router       import router as router_users
from routers.gestiones_router       import router as router_gestiones





api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080","https://gescontfront.herokuapp.com.herokuapp.com"
]
api.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

# Incluimos nuestros dos endpoints en api 
api.include_router(router_clientes)
api.include_router(router_users)
api.include_router(router_gestiones)



""" @api.post("/cliente/registroSave")
async def save_cliente(cliente: Cliente):
    cliente_in_db=ClienteInDB(**cliente.dict())
    return cliente_db.save_cliente(cliente_in_db)

@api.put("/cliente/registroPut")
async def update_cliente(cliente: Cliente):
    cliente_in_db=ClienteInDB(**cliente.dict())
    db_response=cliente_db.update_cliente(cliente_in_db)
    if db_response==None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    else:
        return db_response

@api.delete("/cliente/registroDel/{documento}")
async def delete_cliente(documento: str):
    db_response=cliente_db.delete_cliente(documento)
    if db_response==None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    else:
        return db_response

@api.get("/cliente/registroGet")
async def get_cliente(documento: str):
    cliente_in_db=cliente_db.get_cliente(documento)
    if cliente_in_db==None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    else:
        cliente=Cliente(**cliente_in_db.dict())
        return cliente

@api.get("/cliente/registroGet/{documento}")
async def get_cliente(documento:str):
    cliente_in_db=cliente_db.get_cliente(documento)
    if cliente_in_db==None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    else:
        cliente=Cliente(**cliente_in_db.dict())
        return cliente

@api.get("/cliente/registroGetAll")
async def get_clientes():
    clientes_in_db=cliente_db.get_all_clientes()
    clientes=[]
    for k,v in clientes_in_db.items():
        clientes.append(Cliente(**v.dict()))
    return clientes

@api.get("/")
async def root():
    return {"message":"Gestionatec"} """