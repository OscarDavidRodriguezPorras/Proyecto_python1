from datetime import *

def log(mensaje):
    fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("ERRORES.txt", "a") as archivo:
        archivo.write(f"""
[{fecha}]
{mensaje}""")
    
def act_e(mensaje):
    fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("Actualizaciones.txt", "a") as archivo1:
        archivo1.write(f"""
[{fecha}]
{mensaje}""")

# el a significa agregar sin borrar

