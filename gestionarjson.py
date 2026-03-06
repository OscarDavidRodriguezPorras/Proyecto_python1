import os
import json

def cargar(nombre_archivo_proyecto):
    if not os.path.exists(nombre_archivo_proyecto):
        return []
    try:
        with open(nombre_archivo_proyecto, "r") as archivo1:
            return json.load(archivo1)
    except json.JSONDecodeError:
        return[]
    
def guardar(nombre_archivo_proyecto, datos1):
    with open(nombre_archivo_proyecto, "w") as archivo1:
        json.dump(datos1,archivo1, indent=5)

def generar_id(lista):
    if not lista:
        return 1
    return lista [-1]["Id"] + 1 


