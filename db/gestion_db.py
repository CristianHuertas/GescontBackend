from typing import  Dict
from pydantic import BaseModel


from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from db.db_conexion import Base, engine
from models.cliente_model import Cliente
from db.cliente_db import ClienteInDB

import datetime



class GestionInDB(Base):
    __tablename__ = Cliente.id_cliente

    id_gestion= Column(Integer, primary_key=True, autoincrement=True)
    fecha_gestion= Column(DateTime, default=datetime.datetime.utcnow)
    gestor= Column(String)
    tipificacion= Column(String)
    resumen_gestion= Column(String)
   


Base.metadata.create_all(bind=engine)

