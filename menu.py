from validaciones import *
from registrar_herramientas import *
from registrar_usuarios import *
from gestionar_prestamos import *
from historial import *
def contraseña():
    contraseña_real=123
    contraseña_ingresada=validarEntero("Ingrese la contraseña:")
    if contraseña_ingresada == contraseña_real:
        print("Acceso concedido")
        return True
    else:
        print("CONTRASEÑA INCORRECTA: ")
        return False
    
def menu_principal():
    while True:
        op=validarMenu("""
                    BIENVENIDO
                ESCOGA UNA OPCION
                1. ADMINISTRADOR
                2. USUARIO
                3. SALIR
            """,1,3)
        while op==None:
            op=validarMenu("ERROR, POR FAVOR INGRESE NUEVAMENTE LA OPCION:, ",1,3)
        match op:
            case 1:
                if contraseña():
                    administrador()
            case 2:
                if validar_usuario()==True:
                    solicitar_prestamo()
                else:
                    log("ERROR, Se intento ingresar con un usuario no existente")
                
            case 3:
                print("GRACIAS POR SU TIEMPO")
                print("SALIENDO ...")
            case _:
                print("ERROR, OPCION NO ENCONTRADA POR FAVOR ELIGA UNA: ")
        if op == 3:
            break

def usuario():
    while True:
        op2=validarMenu("""
            POR FAVOR SELECCIONE UNA DE LAS OPCIONES
            1. Agregar usuario
            2. Actualizar usuario
            3. Eliminar usuario
            4. Mostrar usuarios
            5. SALIR
""",1,5)
        while op2==None:
            op2=validarMenu("ERROR, POR FAVOR INGRESE NUEVAMENTE LA OPCION: ",1,3)

        match op2:
            case 1:
                registrar_usuario()
            case 2:
                act_usuario()
            case 3:
                eliminar_usuario()
            case 4:
                listar_usuario()
            case 5:
                print("SALIENDO ...") 
            case _:
                print("OPCION NO ENCONTRADA")
        if op2==5:
            break
   
def administrador():
    while True:
        op3=validarMenu("""
            BIENVENIDO ADMIN, ¿QUE VAMOS A HACER EL DIA DE HOY?
            POR FAVOR ELIGE UNA OPCION PARA PROSEGUIR:
            1. Herramientas
            2. Usuarios
            3. Prestamos
            4. SALIR
""",1,4)
        while op3==None:
            op3=validarMenu("ERROR, INGRESE NUEVAMENTE UNA OPCION CORRECTA: ",1,4)

        match op3:
            case 1:
                menu_h()
            case 2:
                usuario()
            case 3:
                menu_prestamos()
            case 4:
                print("SALIENDO ...")
            case _:
                print("ERROR, INGRESE NUEVAMENTE")
        if op3==4:
            break

def menu_h():
    while True:
        op4=validarMenu("""
                    POR FAVOR ELIGA UNA OPCION
                    1. Registrar Herramientas
                    2. Actualizar Herramienta
                    3. Eliminar Herramienta
                    4. Mostrar Herramientas
                    5. Mostrar stock bajo
                    6. Actualizar estado herramienta
                    7. SALIR
                    """,1,7)
        while op4==None:
                op4=validarMenu("ERROR, INGRESE UNA OPCION CORRECTA: ",1,7)

        match op4:
            case 1:
                registrar_herramienta()
            case 2:
                act_herramienta()
            case 3:
                eliminar_h()
            case 4:
                listar_herramienta()
            case 5:
                stock_bajo()
            case 6:
                actualizar_e_h()
            case 7:
                print("SALIENDO ...")
            case _:
                print("OPCION NO ENCONTRADA")
        if op4==7:
            break


def menu_prestamos():
    while True:
        op5=validarMenu("""
                        ELIGA UNA OPCION
                        1. Estado Prestamo
                        2. Listar prestamo
                        3. Eliminar prestamo
                        4. Historial
                        5. SALIR
""",1,5)
        while op5==None:
            op5=validarMenu("ERROR, INGRESE NUEVAMENTE LA OPCION CORRECTA: ",1,5)

        match op5:
            case 1:
               act_prestamo()
            case 2:
                listar_prestamo()
            case 3:
                eliminar_prestamo()
            case 4: 
                historial()
            case 5:
                print("SALIENDO ...")
            case _:
                print("Opcion no encontrada")
        if op5==5:
            break

def solicitar_prestamo():
    while True:
        op6=validarMenu("""
                        ELIGA UNA DE LAS OPCIONES
                        1. Solicitar prestamo
                        2. SALIR
""",1,2)
        while op6==None:
            op6=validarMenu("Error, por favor ingrese una opcion correcta: ",1,2)
        
        match op6:
            case 1:
                registrar_prestamo()
            case 2:
                print("SALIENDO ...")
            case _:
                print("Opcion no encontrada")
        if op6==2:
            break