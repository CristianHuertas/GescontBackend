from pydantic import BaseModel
from datetime import datetime



class GestionIn(BaseModel):
    
    id_cliente: int
    gestor: str
    tipificacion: str
    resumen_gestion: str

class GestionOut(BaseModel):
    
    id_gestion: int
    id_cliente: int
    fecha_gestion: datetime
    gestor: str
    tipificacion: str
    resumen_gestion: str
    
    class Config:
        orm_mode = True