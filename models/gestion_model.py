from pydantic import BaseModel
import datetime


class GestionInDB(BaseModel):
    
    id_gestion: int
    fecha_gestion: datetime
    gestor: str
    tipificacion: str
    resumen_gestion: str


    class Config:
        orm_mode = True