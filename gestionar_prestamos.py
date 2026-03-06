from gestionarjson import *
from registrar_herramientas import *
from registrar_usuarios import *
from datetime import *
from logs import *
ARCHIVO = "Prestamos.json"

def registrar_prestamo(): 
    prestamos=cargar(ARCHIVO)      
    listar_usuario()
    usuario=cargar("Usuarios.json")
   
    existe=False
    while existe==False:
        id=int(input("Ingrese el id del usuario: "))
        for i in usuario:
            if i["Id"]==id:
                nombre_usuario=usuario[id-1]["Nombre"]
                existe=True 
    listar_herramienta_activo()

    
    herramienta=cargar("Herramientas.json")
    id_h=int(input("Ingrese el id de la herramienta: "))
    existe_h=False
    for elemento in herramienta:
        if elemento["Id"]==id_h and elemento["Estado"]=="Activa":
            nombre_herramienta=herramienta[id_h-1]["Herramienta"]
            cantidad_h=herramienta[id_h-1]["Cantidad"]

            existe_h=True
    if existe_h==False:
        print("La herramienta no existe")
        log(f"""
            ERROR: {nombre_usuario} intento prestar una herramienta que no existe
            """)
        return
    
    print("La cantidad disponible de ", nombre_herramienta, "es: ", cantidad_h)
    cantidad_necesaria=int(input("Ingrese la cantidad de herramientas que necesita: "))
    
    while cantidad_h < cantidad_necesaria:
            print("Stock insuficiente solo hay disponible: ", cantidad_h)
            cantidad_necesaria=int(input("Ingrese la cantidad adecuada: "))
            log(f"""    
                ERROR: {nombre_usuario} intento prestar {cantidad_necesaria} de {nombre_herramienta}
                Hay disponibles: {cantidad_h}
                """)
            return
    
    act_stock(id_h,cantidad_h,cantidad_necesaria)
  
    fecha_creacion=datetime.now()
    fecha_creacion_j=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    dias_prestamo=int(input("Ingrese cantidad de dias de prestamo: "))
    fecha_final_prestamo=fecha_creacion+timedelta(days=dias_prestamo)
    if datetime.now()<fecha_final_prestamo:
        estado_prestamo=("Activo")
    else:
        estado_prestamo=("Vencido")
    
    estado=("Pendiente")

    nuevo_prestamo={
        "Id":generar_id(prestamos),
        "Usuario":nombre_usuario,
        "Herramienta":nombre_herramienta,
        "Cantidad":cantidad_necesaria,
        "Fecha_c":fecha_creacion_j,
        "Fecha_f":str(fecha_final_prestamo),
        "Estado":estado,
        "Es_prestamo":estado_prestamo
    }
    prestamos.append(nuevo_prestamo)
    guardar(ARCHIVO, prestamos)

def listar_prestamo():
    prestamos=cargar(ARCHIVO)

    if not prestamos:
        print("No hay prestamos realizados")
    
    for elemento in prestamos:
        print("*************************************************")
        print(f"""
            Id:                                {elemento["Id"]}
            Usuario:                           {elemento["Usuario"]}
            Herramienta:                       {elemento["Herramienta"]}
            Cantidad:                          {elemento["Cantidad"]}
            Fecha creacion:                    {elemento["Fecha_c"]}
            Fecha vencimiento prestamo:        {elemento["Fecha_f"]}
            Estado:                            {elemento["Estado"]}
            Estado prestamo:                   {elemento["Es_prestamo"]}
    """)
        
def act_prestamo():
    prestamos=cargar(ARCHIVO)
    listar_prestamo()
    id_prestamo=validarEntero("Escoja el id del prestamo a actualizar: ")
    while (id_prestamo==None):
        id_prestamo=validarEntero("Error, Escoja el id del prestamo a actualizar: ")


    for elemento in prestamos:
        if id_prestamo==elemento["Id"]:
            estado_p1=prestamo_estado()
            elemento["Estado"]=estado_p1
            guardar(ARCHIVO, prestamos)
            print("Estado actualizado")
            return
        else:
            log("ERROR: el administrador trato de buscar un prestamo inexistente")
            
def prestamo_estado():
    while True:
        estado_herramienta=int(input("""
                                    INGRESE EL ESTADO DE LA HERRAMIENTA
                                    1. Pendiente
                                    2. Activo
                                    """))
        if estado_herramienta==1:
            return("Pendiente")
        elif estado_herramienta==2:
            return("Activo")
        else: 
            estado_herramienta=int(input("Ingrese nuevamente la opcion: "))
            log("ERROR:  el administrador trato de cambiar el estado del prestamo a uno inexistente")   

def eliminar_prestamo():
    contador_aux=0
    prestamos=cargar(ARCHIVO)
    listar_prestamo()
    id_prestamo=validarEntero("Ingrese el id del prestamo a eliminar: ")
    while(id_prestamo==None):
        id_prestamo=validarEntero("Error, ingrese el id correcto: ")
    
    for elemento in prestamos:
        if id_prestamo==elemento["Id"]:
            prestamos.pop(contador_aux)
            guardar(ARCHIVO, prestamos)
            print("PRESTAMO ELIMINADO CON EXITO")
            return
        contador_aux+=1
    print("El prestamo no existe")
    log("ERROR: el administrador trato de eliminar un prestamo inexistente")