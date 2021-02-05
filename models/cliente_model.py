from pydantic import BaseModel

class Cliente(BaseModel):
    
    id_cliente: int
    documento: int
    razon_social: str
    contacto: str
    telefono: str
    ciudad: str
    correo: str
    detalle: str

    class Config:
        orm_mode = True
