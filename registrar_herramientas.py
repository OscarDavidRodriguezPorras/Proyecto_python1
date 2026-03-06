from gestionarjson import cargar, guardar, generar_id
from validaciones import validarEntero, validarMenu, nombre_valido
from datetime import date, datetime
from logs import *

ARCHIVO="Herramientas.json"

def p_categoria():
    while True:
        categoria_op=int(input("""
                            Ingrese la categoria
                            1. Construccion 
                            2. Jardineria
                            """))
        if categoria_op==1:
            return ("Construccion")
        elif categoria_op==2:
            return ("Jardineria")
        else:
            categoria_op=int(input("Error, opcion no valida: "))

def op_estado():
    while True:
        estado_op=int(input("""
                            Ingrese el estado de la herramienta
                            1. Activa
                            2. En reparacion
                            3. Fuera de servicio
                            """))
        if estado_op==1:
            return ("Activa")
        elif estado_op==2:
            return ("En reparacion")
        elif estado_op==3:
            return ("Fuera de servicio")
        else:
            estado_op=int(input("ERROR, INGRESE NUEVAMENTE LA OCPION: "))

def registrar_herramienta():
    herramientas = cargar(ARCHIVO)

    nombre_h=input("Por favor ingrese el nombre de la herramienta a agregar: ")
    while nombre_valido(nombre_h)==False or existe_herramienta(nombre_h)==True:
        nombre_h=input("Ingrese el nombre de la herramienta valida: ")
    cantidad_h=validarEntero("Ingrese la cantidad en stock: ")
    categoria=p_categoria()
    estado=op_estado()
    valor_h=validarEntero("Ingrese el valor de la herramienta: ")
    fecha_creacion=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nueva_herramienta={
        "Id":generar_id(herramientas),
        "Herramienta": nombre_h,
        "Cantidad":cantidad_h,
        "Categoria":categoria,
        "Estado":estado,
        "Valor":valor_h,
        "Fecha":fecha_creacion
    }
    herramientas.append(nueva_herramienta)
    guardar(ARCHIVO, herramientas)
    print("HERRAMIENTA AÑADIDA CON EXITO")
    return categoria, estado

def listar_herramienta():
    herramientas=cargar(ARCHIVO)

    if not herramientas:
        print("No hay herramientas registradas\n")
        return[]
    
    for elemento in herramientas:
        print("***************************************")
        print(f"Id:                {elemento['Id']}")
        print(f"Herramienta:       {elemento['Herramienta']}")
        print(f"Disponibles:       {elemento['Cantidad']}")
        print(f"Categoria:         {elemento['Categoria']}")
        print(f"Estado:            {elemento["Estado"]}")
        print(f"Valor herramienta: ${elemento["Valor"]}")
        print(f"Fecha creacion:    {elemento["Fecha"]}")
    print()

def listar_herramienta_activo():
    herramientas=cargar(ARCHIVO)
    
    if not herramientas:
        print("No hay herramientas activas")
        return
    
    for elemento in herramientas:
        if elemento["Estado"]=="Activa":

            print("***************************************")
            print(f"Id:                {elemento['Id']}")
            print(f"Herramienta:       {elemento['Herramienta']}")
            print(f"Disponibles:       {elemento['Cantidad']}")
            print(f"Categoria:         {elemento['Categoria']}")
            print(f"Estado:            {elemento["Estado"]}")
            print(f"Valor herramienta: ${elemento["Valor"]}")
            print(f"Fecha creacion:    {elemento["Fecha"]}")
        print()

def existe_herramienta(nombre_h):
    herramientas = cargar(ARCHIVO)
    for elemento in herramientas:
        if nombre_h.lower()==elemento["Herramienta"].lower():
            return True
    return False

def act_herramienta():
    herramientas=cargar(ARCHIVO)
    listar_herramienta()
    id_herramienta=validarEntero("Escoja el id de la herramienta a actualizar: ")
    while(id_herramienta==None):
        id_herramienta=validarEntero("ERROR, Escoja el id de la herramienta a actualizar: ")

    for elemento in herramientas:
        if id_herramienta==elemento["Id"]:
            nombre_h=input("Ingrese el nombre de la herramienta: ")
            while nombre_valido(nombre_h)==False:
                nombre_h=input("Error, ingrese el nombre de la herramienta: ")
            elemento["Herramienta"]=nombre_h
            guardar(ARCHIVO, herramientas)
            print("Herramienta actualizada")
            return

def act_stock(Id,cantidad_ant, cantidad_nec):
    herramientas=cargar(ARCHIVO)
    for elemento in herramientas:
        if Id==elemento["Id"]:
            elemento["Cantidad"]=cantidad_ant-cantidad_nec
            if elemento["Cantidad"]==0:
                elemento["Estado"]="Fuera de servicio"
            guardar(ARCHIVO, herramientas)
            print("Cantidad actualizada")
            return

def eliminar_h():
    contador_aux=0
    herramientas=cargar(ARCHIVO)
    listar_herramienta()
    id_herramienta=validarEntero("Escoja el id de la herramienta a eliminar")
    while(id_herramienta==None):
        id_herramienta=validarEntero("Error, escoja el id de la herramienta a eliminar")

    for elemento in herramientas:
        if id_herramienta==elemento["Id"]:
            herramientas.pop(contador_aux)
            guardar(ARCHIVO, herramientas)
            print("HERRAMIENTA ELIMINADA CON EXITO")
            return
        contador_aux+=1
    print("La herramienta no existe")

def stock_bajo():
    herramientas=cargar(ARCHIVO)

    if not herramientas:
        print("No hay Herramientas")
        return
    
    for elemento in herramientas:
        if elemento["Cantidad"]<3:

            print("******************************************")
            print(f"""
                    HERRAMIENTAS CON STOCK BAJO
                Id:                {elemento['Id']}  
                Herramienta:       {elemento['Herramienta']}
                Disponibles:       {elemento['Cantidad']}
                Categoria:         {elemento['Categoria']}
                Estado:            {elemento["Estado"]}
                Valor herramienta: ${elemento["Valor"]}
                Fecha creacion:    {elemento["Fecha"]}
                    """)

def actualizar_e_h():
    herramientas=cargar(ARCHIVO)
    listar_herramienta()
    id_h=validarEntero("Escoja el id de la herramienta a actualziar: ")
    while(id_h==None):
        id_h=validarEntero("Error: ingrese nuevamente: ")

    for elemento in herramientas:
        if id_h==elemento["Id"]:
                estado_op=int(input("""
                                    Ingrese el estado de la herramienta:
                                    1. Activa
                                    2. En reparacion
                                    3. Fuera de servicio
                                    """))
                if estado_op==1:
                    estado_op="Activa"
                elif estado_op==2:
                    estado_op="En reparacion"
                elif estado_op==3:
                    estado_op="Fuera de servicio"
                else:
                    estado_op=int(input("ERROR, INGRESE NUEVAMENTE LA OCPION: "))

                elemento["Estado"]=estado_op
                nombre_herramienta=elemento["Herramienta"]
                guardar(ARCHIVO, herramientas)
                print("Estado herramienta actualizada")
                act_e(f"""Accion: {estado_op}
La herramienta {nombre_herramienta} fue actualizada a {estado_op}
""")
                return
        

