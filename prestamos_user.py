import json
import os
import prestamos_admin
import gestion_herramientas
import menus
archivo_prestamo = "prestamos.json"

archivo_herramientas = "herramientas.json"

def cargar_datos(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_archivos(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)


def menu():
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