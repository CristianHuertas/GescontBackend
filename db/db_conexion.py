from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

#Creando Motor y Conexion con la Base de Datos
# TODO: Con la ayuda de pgAdmin debes crear una base de datos
# y la BD debes crearle un esquema
# TODO: Debes cambiar con tu usuario y contraseña de PostgreSQL
# además del host, puerto y nombre de la base de datos que hayas definido
import os


#DATABASE_URL = os.environ['DATABASE_URL']


SQLALCHEMY_DATABASE_URL = "postgres://lokaqpupicdmkq:31e27bea81a63ef0f4cc16385618377c2c5f280fa1a1ee5d73b5a96a5de6fb3b@ec2-34-230-167-186.compute-1.amazonaws.com:5432/d9t0gdio17cala"

engine                  = create_engine(SQLALCHEMY_DATABASE_URL)
#engine = create_engine(DATABASE_URL)

#Creacion de un creador la Sesion
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

# En obtener_sesion inyectamos la dependencia SessionLocal
def obtener_sesion():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creando Base para la creacion de los modelos
Base = declarative_base()

# TODO: Reemplazar el nombre del esquema creado 
# en la base de datos
Base.metadata.schema = "gescont"