"""Módulo de gestión de préstamos para residentes.

Proporciona un menú simplificado que delega las operaciones
de registro y devolución al módulo de administración de préstamos.
"""

import os
from . import prestamos_admin
from . import menus

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
archivo_prestamo = os.path.join(DATA_DIR, "prestamos.json")
archivo_herramientas = os.path.join(DATA_DIR, "herramientas.json")


def menu():
    """Muestra el menú de préstamos para residentes.

    Opciones: registrar préstamo, devolver préstamo o volver al menú anterior.
    Las operaciones son delegadas a prestamos_admin.
    """
    print("\n---------- MENU PRESTAMOS RESIDENTE ----------")
    print("\n1. Registrar préstamo.")
    print("\n2. Devolver préstamo.")
    print("\n0. Volver al menú principal.")

    res = int(input("\nIngrese una opción: "))

    if res == 1:
        prestamos_admin.registrar_prestamo()
    elif res == 2:
        prestamos_admin.devolver_prestamo()
    elif res == 0:
        menus.menu_residente()
