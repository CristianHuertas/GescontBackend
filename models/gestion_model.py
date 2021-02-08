from pydantic import BaseModel
import datetime


class Gestion(BaseModel):
    
    id_gestion: int
    id_cliente: int
    fecha_gestion: datetime
    gestor: str
    tipificacion: str
    resumen_gestion: str


    class Config:
        orm_mode = True