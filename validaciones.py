def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None
    
def validarMenu(mensaje, min, max):
    try: 
        dato=int(input(mensaje))
        if dato<min or dato>max:
            return None
        else:
            return dato
    except:
        return None
    
def nombre_valido(nombre):
    if nombre.strip()=="":
        print("Nombre Vacio")
        return False
    return True

