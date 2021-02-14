from pydantic import BaseModel
from datetime import datetime



class Gestion(BaseModel):
    
    id_gestion: int
    id_cliente: int
    fecha_gestion: str
    gestor: str
    tipificacion: str
    resumen_gestion: str

    class Config:
        orm_mode = True