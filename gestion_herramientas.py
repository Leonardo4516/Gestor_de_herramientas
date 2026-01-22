import json
import os
import menus

asd = "herramientas.json"

    
def cargar_herramientas(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    
    return []
    
def guardar_herramientas(archivo, lista):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4)

def generar_id(lista):
    if not lista:
        return 1
    return max(h["id"] for h in lista) + 1

def gestion_admin():

    print("\n---------- AGREGAR/CREAR HERRAMIENTA ----------")

    herramientas = cargar_herramientas(asd)

    herramienta = {
        "id" : generar_id(herramientas),
        "nombre" : input("Nombre de la herramienta: "),
        "categoria" : input("Categoría (construcción, jardinería, etc): "),
        "cantidad" : int(input("Cantidad disponible: ")),
        "estado" : input("Estado (activa / en reparación / fuera de servicio): "),
        "valor" : float(input("Valor estimado: "))
    }

    herramientas.append(herramienta)
    guardar_herramientas(asd, herramientas)

    print("\nHerramienta creada correctamente.")

    menus.menu_admin()

def listar_herramientas():
    print("\n---------- LISTAR HERRAMIENTA ----------")

    if os.path.exists(asd):
        herramientas = cargar_herramientas(asd)
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
        return
     
        
def buscar_herramientas():

    print("\n---------- BUSCAR HERRAMIENTA ----------")


    herramientas = cargar_herramientas(asd)

    buscar_id = int(input("Ingrese el ID de la herramienta: "))

    for a in herramientas:
        if a["id"] == buscar_id:
            print(a)
            menus.menu_admin()
            return
            
    print("Herramienta no encontrada.")
    menu()

def actualizar_herramientas():
    herramientas = cargar_herramientas(asd)
    buscar_id = int(input("Ingrese el ID de la herramienta: "))

    for a in herramientas:
        if a["id"] == buscar_id:
            a["nombre"] = input("Nuevo nombre: ")
            a["categoria"] = input("Nueva categoría: ")
            a["cantidad"] = int(input("Nueva cantidad: "))
            a["estado"] = input("Nuevo estado: ")
            a["valor"] = float(input("Nuevo valor estimado: "))

            guardar_herramientas(asd, herramientas)
            print("Herramienta actualizada.")
            return
    print("Herramienta no encontrada.")

def eliminar_herramienta():

    print("\n---------- ELIMINAR HERRAMIENTA ----------")
    
    herramientas = cargar_herramientas(asd)
    buscar_id = int(input("\nIngrese el ID de la herramienta: "))

    for a in herramientas:
        if a["id"] == buscar_id:
            opcion = input("¿Eliminar o incativar? (E/I): ").lower()

            if opcion == "e":
                herramientas.remove(a)
                print("Herramienta eliminada.")
                menus.menu_admin()
            elif opcion == "i":
                a["estado"] = "fuera de servicio"
                print("Herramienta inactivada.")
                
            guardar_herramientas(asd, herramientas)
            menus.menu_admin()
            return
    
    print("\nHerramienta no encontrada. Intente de nuevo.")
    menu()

def menu():
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