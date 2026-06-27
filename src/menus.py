"""Módulo de menús de navegación.

Define los menús principal de administrador y de residente,
redirigiendo a los módulos correspondientes según la opción elegida.
"""

from . import gestion_herramientas, gestion_usuarios, prestamos_admin
from . import prestamos_user, inicio_sesion


def menu_admin():
    """Muestra el menú principal del administrador.

    Opciones: gestión de usuarios, herramientas, préstamos y reparación.
    """
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
    elif res == 0:
        print("\nSaliendo del menú.")
        inicio_sesion.inicio_sesion()
    else:
        print("No se ingresó un valor válido. Intente de nuevo.")
        menu_admin()


def menu_residente():
    """Muestra el menú principal del residente.

    Opciones: consultar herramientas y gestión de préstamos.
    """
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
