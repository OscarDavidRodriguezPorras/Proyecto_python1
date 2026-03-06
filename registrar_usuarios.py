from validaciones import *
from gestionarjson import *
from datetime import *

ARCHIVO = "Usuarios.json"

def tipo_usuario():
    while True:
        t_usu=int(input("""
                        ESCOGA EL TIPO DE USUARIO
                            ¡SOLO EL NUMERO!
                        1. Administrador
                        2. Usuario
                        """))
        if t_usu==1:
            print("La contraseña para ingresar al apartado ADMINISTRADOR ES: 123")
            return ("Administrador")
        elif t_usu==2:
            return ("Usuario")
        else:
            t_usu=int(input("ERROR, por favor ingrese una opcion correcta: "))

def telefono_c():
    telefono_u=int(input("Ingrese el numero telefonico: "))
    while telefono_u < 1000000000 or telefono_u>9999999999:
        if telefono_u<1000000000:
            telefono_u=int(input("El numero debe tener 10 caracteres: "))
        else: 
            telefono_u=int(input("El numero no puede pasar los 10 caracteres: "))
    return telefono_u

def registrar_usuario():
    usuarios = cargar(ARCHIVO)

    nombre_u=input("Por favor ingrese su nombre: ")
    while nombre_valido(nombre_u)==False or existe_usuario(nombre_u)==True:
        nombre_u=input("Ingrese un nombre valido: ")
    apellido_u=input("Por favor ingrese el apellido: ")
    while nombre_valido(apellido_u)==False or existe_usuario(apellido_u)==True:
        apellido_u=input("Ingrese un nombre apellido valido: ")
    telefono_u=telefono_c()
    direccion_u=input("Ingrese su direccion: ")
    usuario=tipo_usuario()
    fecha_c_u=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nuevo_usuario={
        "Id":generar_id(usuarios),
        "Nombre":nombre_u,
        "Apellido":apellido_u,
        "Telefono":telefono_u,
        "Direccion":direccion_u,
        "Tipo":usuario,
        "Fecha":fecha_c_u
    }
    usuarios.append(nuevo_usuario)
    guardar(ARCHIVO, usuarios)
    print("USUARIO AGREGADO CON EXITO")
    return usuario, telefono_u

def listar_usuario():
    usuarios=cargar(ARCHIVO)

    if not usuarios:
        print("No hay usuarios registrados")
        return
    
    for elemento in usuarios:
        print("**************************************")
        print(f"""
            Id:                {elemento["Id"]}
            Nombre:            {elemento["Nombre"]}
            Apellido:          {elemento["Apellido"]}
            Telefono:          {elemento["Telefono"]}
            Direccion:         {elemento["Direccion"]}
            Tipo usuario:      {elemento["Tipo"]}
            Fecha              {elemento["Fecha"]}
""")

def existe_usuario(nombre_u):
    usuarios=cargar(ARCHIVO)
    for elemento in usuarios:
        if nombre_u.lower()==elemento["Nombre"].lower():
            return True
    return False

def act_usuario():
    usuarios=cargar(ARCHIVO)
    listar_usuario()
    id_usuario=validarEntero("Escoja el id del usuario a actualizar: ")
    while (id_usuario==None):
        id_usuario=id_usuario=validarEntero("ERROR, escoja el id del usuario a actualizar: ")
    
    for elemento in usuarios:
        if id_usuario==elemento["Id"]:
            nombre_u=input("Ingrese el nombre del usuario a actualizar: ")
            while nombre_valido(nombre_u)==False:
                nombre_u=input("ERROR, ingrese el nombre del usuario a actualizar: ")
            elemento["Nombre"]=nombre_u
            guardar(ARCHIVO, usuarios)
            print("USUARIO ACTUALIZADO CON EXITO")
            return
        
def eliminar_usuario():
    contador_aux=0
    usuarios=cargar(ARCHIVO)
    listar_usuario()
    id_usuario=validarEntero("Ingrese el id del usuario a eliminar: ")
    while(id_usuario==None):
        id_usuario=validarEntero("Error, ingrese el id del usuario a eliminar: ")

    for elemento in usuarios:
        if id_usuario==elemento["Id"]:
            usuarios.pop(contador_aux)
            guardar(ARCHIVO, usuarios)
            print("USUARIO ELIMINADO CON EXITO")
            return
        contador_aux+=1
    print("El usuario no existe")

def validar_usuario():
    usuario=cargar(ARCHIVO)
    nombre=input("Ingrese el nombre su nombre: ").strip()

    for elemento in usuario:
        if elemento["Nombre"].lower()==nombre.lower():
            print("Usuario encontrado")
            return True
    print("ERROR: el usuario no existe")
    return False

