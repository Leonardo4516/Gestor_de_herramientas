import gestion_herramientas
import gestion_usuarios
import prestamos_admin
import prestamos_user
import inicio_sesion
#import registros_reparacion

def menu_admin():

    print("\n---------- MENU DE ADMIN ----------")
    print("\n1. Opciones de usuario.")
    print("\n2. Opciones de herramientas.")
    print("\n3. Opciones de prestamos.")
    print("\n4. Opciones de reparación.")
    print("\n0. Salir")

    res = int(input("\nIngrese una opción (0-3): "))

    if res == 1:
        gestion_usuarios.menu_gestion_us()
    elif res == 2:
        gestion_herramientas.menu()
    elif res == 3:
        prestamos_admin.menu()
    #elif res == 4:
    #    registros_reparacion.menu()
    elif res == 0:
        print("\nSaliendo del menú.")
        inicio_sesion.inicio_sesion()
    else: 
        print("No se ingresó un valor válido. Intente de nuevo.")
        menu_admin()
        



    
def menu_residente():

    print("\n---------- MENU DE RESIDENTE ----------")
    print("\n1. Consultar herramientas.")
    print("\n2. Opciones prestamos.")
    print("\n0. Salir.")

    res = int(input("\nIngrese una opción (0-2): "))

    if res == 1:
        gestion_herramientas.listar_herramientas()
        menu_residente()
    elif res == 2:
        prestamos_user.menu()
        menu_residente()
    elif res == 0:
        print("Saliendo del menú.")
        inicio_sesion.inicio_sesion()
        



