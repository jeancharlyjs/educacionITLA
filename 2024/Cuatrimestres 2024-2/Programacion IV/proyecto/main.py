from fastapi import FastAPI, Form, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import sqlite3 as s
import json

import pandas as pd
#Instanciar la FasAPI

app = FastAPI()

# Schema

class Formulario(BaseModel):
    nombre: str
    titulo: str
    # categoria: list

#Configurar el Template

templates = Jinja2Templates(directory='templates')



biblioteca = [
        {'nombre': 'nombre1', 'titulo': 'titulo1', 'categoria': 'Ciencia'},
        {'nombre': 'nombre2', 'titulo': 'titulo2', 'categoria': 'Arte'},
        {'nombre': 'nombre3', 'titulo': 'titulo3', 'categoria': 'Matematica'}
        ]

@app.get("/")
def index(request: Request):
    return  templates.TemplateResponse("index.html", {'request': request})


@app.get('/endpoint')
def endpoints():
    return biblioteca

@app.get("/registro_libro/")
def formulario(request: Request):
    return templates.TemplateResponse("formularios/formulario.html", {"request": request})


@app.post("/registro_libro/")
async def formularioRegistro(request: Request):
    datosFormulario = await request.form()
    datosDiccionario = dict(datosFormulario)

    conn = s.connect("BaseDB.db")
    cursor = conn.cursor()
    datos = [(datosDiccionario['nombre'], datosDiccionario['titulo'])]
    print(datos)

    cursor.executemany("INSERT INTO libreria VALUES(?, ?)", datos)
    conn.commit()
    conn.close()

    print(datosDiccionario)



@app.get('/libros_registrados')
def librosRegistrados(request: Request):
    diccionario = []
    conn = s.connect("BaseDB.db")
    cursor = conn.cursor()

    query = """SELECT * FROM libreria"""
    df = pd.read_sql(query, conn)
    diccionario.append(df.to_dict())
    return diccionario

