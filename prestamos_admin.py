import json
import os
from datetime import date
import menus
from logs import anotar_evento

archivo_prestamos = "prestamos.json"
archivo_herramientas = "herramientas.json"

def cargar_datos(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_datos(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

def generar_id(lista):
    return max((a["id"] for a in lista), default=0) + 1

def registrar_prestamo():

    print("\n---------- REGISTRAR PRÉSTAMO ----------")

    prestamos = cargar_datos(archivo_prestamos)
    herramientas = cargar_datos(archivo_herramientas)

    usuario = input("\nUsuario: ")
    herramienta_id = int(input("\nID de la herramienta: "))
    cantidad = int(input("\nCantidad a prestar: "))
    observaciones = input("\nObservaciones: ")

    for a in herramientas:
        if a["id"] == herramienta_id:
            if a["estado"] != "activa":
                print("\nLa herramienta no está activa.")
                return
            
            elif a["cantidad"] < cantidad:
                print("\nNo hay suficiente stock.")

            a["cantidad"] -= cantidad

            prestamo = {
                "id" : generar_id(prestamos),
                "usuario" : usuario,
                "herramienta_id" : herramienta_id,
                "cantidad" : cantidad,
                "fecha_inicio" : str(date.today()),
                "fecha_devolucion" : input("Fecha estimada de devolución (DD-MM-YYYY): "),
                "estado" : "activo",
                "observaciones" : observaciones
            }

            prestamos.append(prestamo)

            guardar_datos(archivo_herramientas, herramientas)

            guardar_datos(archivo_prestamos, prestamos)

            anotar_evento("PRÉSTAMO", f"Préstamo registrado para la herramienta ID {herramienta_id}.", usuario)

            print("Préstamo registrado correctamente.")
            return
        
    print("Herramienta no encontrada.")

def devolver_prestamo():
    
    print("\n---------- DEVOLVER PRESTAMO ----------")

    prestamo = cargar_datos(archivo_prestamos)

    herramientas = cargar_datos(archivo_herramientas)

    prestamo_id = int(input("\nID del préstamo: "))

    for p in prestamo:
        if p["id"] == prestamo_id and p["estado"] == "activo":

            # Restaurar stock
            for h in herramientas:
                if h["id"] == p["herramienta_id"]:
                    h["cantidad"] += p["cantidad"]
                    break

            p["estado"] = "devuelto"

            guardar_datos(archivo_herramientas, herramientas)
            guardar_datos(archivo_prestamos, prestamo)

            anotar_evento("DEVOLUCIÓN", f"Préstamo ID {prestamo_id} devuelto.", p["usuario"])

            print("Préstamo devuelto correctamente.")
            return

    print("Préstamo no encontrado o ya devuelto.")

def listar_prestamos():

    print("\n---------- LISTAR PRESTAMOS ----------")

    prestamos = cargar_datos(archivo_prestamos)

    if not prestamos:
        print("No hay préstamos registrados.")
        menu()
        return

    for p in prestamos:
        print(f"""
        ---------------------------
        ID: {p['id']}
        Usuario: {p['usuario']}
        Herramienta ID: {p['herramienta_id']}
        Cantidad: {p['cantidad']}
        Inicio: {p['fecha_inicio']}
        Devolución: {p['fecha_devolucion']}
        Estado: {p['estado']}
        Observaciones: {p['observaciones']}
        ---------------------------
        """)
        
    menu()

        
def menu():
    print("\n---------- MENU PRESTAMOS ADMIN ----------")
    print("\n1. Registrar préstamo.")
    print("\n2. Devolver préstamo.")
    print("\n3. Listar prestamo.")
    print("\n0. Volver al menú principal.")

    res = int(input("\nIngrese una opción: "))

    if res == 1:
        registrar_prestamo()
    elif res == 2:
        devolver_prestamo()
    elif res == 3:
        listar_prestamos()
    elif res == 0:
        menus.menu_admin()