"""Módulo de gestión de herramientas.

Proporciona operaciones CRUD para el inventario de herramientas
del taller: crear, listar, buscar, actualizar y eliminar.
"""

import json
import os
from . import menus
from .logs import anotar_evento

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
RUTA_HERRAMIENTAS = os.path.join(DATA_DIR, "herramientas.json")


def cargar_herramientas(archivo):
    """Carga la lista de herramientas desde un archivo JSON.

    Args:
        archivo: Ruta al archivo JSON de herramientas.

    Returns:
        Lista de diccionarios con los datos de las herramientas,
        o lista vacía si el archivo no existe.
    """
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_herramientas(archivo, lista):
    """Guarda la lista de herramientas en un archivo JSON.

    Args:
        archivo: Ruta al archivo JSON de herramientas.
        lista: Lista de diccionarios a guardar.
    """
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4)


def generar_id(lista):
    """Genera un ID autoincremental para una nueva herramienta.

    Args:
        lista: Lista de herramientas existentes.

    Returns:
        ID numérico siguiente al máximo existente, o 1 si está vacía.
    """
    if not lista:
        return 1
    return max(h["id"] for h in lista) + 1


def gestion_admin():
    """Registra una nueva herramienta en el inventario."""
    print("\n---------- AGREGAR/CREAR HERRAMIENTA ----------")

    herramientas = cargar_herramientas(RUTA_HERRAMIENTAS)

    herramienta = {
        "id": generar_id(herramientas),
        "nombre": input("Nombre de la herramienta: "),
        "categoria": input("Categoría (construcción, jardinería, etc): "),
        "cantidad": int(input("Cantidad disponible: ")),
        "estado": input("Estado (activa / en reparación / fuera de servicio): "),
        "valor": float(input("Valor estimado: ")),
    }

    herramientas.append(herramienta)
    guardar_herramientas(RUTA_HERRAMIENTAS, herramientas)

    anotar_evento("CREACIÓN", "Nueva herramienta agregada.", herramienta["nombre"])
    print("\nHerramienta creada correctamente.")
    menus.menu_admin()


def listar_herramientas():
    """Muestra todas las herramientas registradas en el inventario."""
    print("\n---------- LISTAR HERRAMIENTA ----------")

    if os.path.exists(RUTA_HERRAMIENTAS):
        herramientas = cargar_herramientas(RUTA_HERRAMIENTAS)
        for a in herramientas:
            print(f"""
            -----------------------
            ID : {a["id"]}
            Nombre: {a["nombre"]}
            Categoría: {a["categoria"]}
            Cantidad: {a["cantidad"]}
            Estado: {a["estado"]}
            Valor: {a["valor"]}
            -----------------------
            """)
    else:
        print("No hay herramientas registradas.")
        menus.menu_admin()


def buscar_herramientas():
    """Busca una herramienta por su ID y muestra su información."""
    print("\n---------- BUSCAR HERRAMIENTA ----------")

    herramientas = cargar_herramientas(RUTA_HERRAMIENTAS)
    buscar_id = int(input("Ingrese el ID de la herramienta: "))

    for a in herramientas:
        if a["id"] == buscar_id:
            print(a)
            menus.menu_admin()
            return

    print("Herramienta no encontrada.")
    menu()


def actualizar_herramientas():
    """Actualiza los datos de una herramienta existente por su ID."""
    herramientas = cargar_herramientas(RUTA_HERRAMIENTAS)
    buscar_id = int(input("Ingrese el ID de la herramienta: "))

    for a in herramientas:
        if a["id"] == buscar_id:
            a["nombre"] = input("Nuevo nombre: ")
            a["categoria"] = input("Nueva categoría: ")
            a["cantidad"] = int(input("Nueva cantidad: "))
            a["estado"] = input("Nuevo estado: ")
            a["valor"] = float(input("Nuevo valor estimado: "))

            guardar_herramientas(RUTA_HERRAMIENTAS, herramientas)
            print("Herramienta actualizada.")
            return

    print("Herramienta no encontrada.")


def eliminar_herramienta():
    """Elimina o inactiva una herramienta del inventario por su ID."""
    print("\n---------- ELIMINAR HERRAMIENTA ----------")

    herramientas = cargar_herramientas(RUTA_HERRAMIENTAS)
    buscar_id = int(input("\nIngrese el ID de la herramienta: "))

    for a in herramientas:
        if a["id"] == buscar_id:
            opcion = input("¿Eliminar o inactivar? (E/I): ").lower()

            if opcion == "e":
                herramientas.remove(a)
                anotar_evento("ELIMINACIÓN", "Herramienta eliminada.", a["nombre"])
                print("Herramienta eliminada.")
                menus.menu_admin()
            elif opcion == "i":
                a["estado"] = "fuera de servicio"
                anotar_evento("INACTIVACIÓN", "Herramienta inactivada.", a["nombre"])
                print("Herramienta inactivada.")

            guardar_herramientas(RUTA_HERRAMIENTAS, herramientas)
            menus.menu_admin()
            return

    print("\nHerramienta no encontrada. Intente de nuevo.")
    menu()


def menu():
    """Muestra el menú de gestión de herramientas."""
    print("\n---------- MENU DE GESTIÓN DE HERRAMIENTAS ----------")
    print("\n1. Crear/Agregar herramientas.")
    print("\n2. Listar herramientas.")
    print("\n3. Buscar herramientas.")
    print("\n4. Actualizar herramientas")
    print("\n5. Eliminar herramienta.")
    print("\n0. Volver a menú principal.")

    res = int(input("\nIngrese una opción: "))

    if res == 1:
        gestion_admin()
    elif res == 2:
        listar_herramientas()
        menu()
    elif res == 3:
        buscar_herramientas()
    elif res == 4:
        actualizar_herramientas()
    elif res == 5:
        eliminar_herramienta()
    elif res == 0:
        menus.menu_admin()
    else:
        print("No se ingresó un valor válido. Intente de nuevo.")
        menu()
