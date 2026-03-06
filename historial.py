from gestionarjson import *
ARCHIVO = "Historial.json"

def historial():
    prestamos=cargar("Prestamos.json")
    nombre = input("Ingrese el nombre del usuario: ").strip()
    historial=cargar(ARCHIVO)
    
    encontrado=False

    print(f"Historial de prestamos de {nombre}:")

    for elemento in prestamos:
        if elemento["Usuario"].lower() == nombre.lower():
            encontrado= True
            print("****************************************")
            print(f"""
                Id:               {elemento["Id"]}
                Herramienta:      {elemento["Herramienta"]}
                Cantidad:         {elemento["Cantidad"]}
                Fecha inicio:     {elemento["Fecha_c"]}
                Fecha fin:        {elemento["Fecha_f"]}
                Estado:           {elemento["Estado"]}
""")
            
    if not encontrado:
        print("El usuario no tiene prestamos registrados")





