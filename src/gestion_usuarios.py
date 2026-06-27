"""Módulo de gestión de usuarios residentes.

Proporciona operaciones CRUD para los usuarios del sistema:
crear, listar, modificar información y eliminar residentes.
"""

import json
import os
from . import menus
from .logs import anotar_evento

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def eliminar_us():
    """Elimina un usuario residente del sistema.

    Busca al usuario por nombre, muestra su información,
    solicita confirmación y lo elimina tanto del registro
    de datos como del archivo de contraseñas.
    """
    print("\n---------- ELIMINAR USUARIO ----------")

    try:
        with open(os.path.join(DATA_DIR, "residente_r.json"), "r", encoding="utf-8") as f:
            reg_el = json.load(f)

        with open(
            os.path.join(DATA_DIR, "contraseñas_residente.json"), "r", encoding="utf-8"
        ) as e:
            contra_el = json.load(e)

        user = input("Ingrese el nombre del usuario: ")

        registro_actualizado = [
            r for r in reg_el if r["Nombres"] != user
        ]
        contra_actualizada = [
            c for c in contra_el if c["Nombres"] != user
        ]

        verificar_registro = next(
            (r for r in reg_el if r["Nombres"] == user), None
        )

        if verificar_registro is None:
            print("Usuario no encontrado.")
            eliminar_us()
            return

        print("\nInformación encontrada en base a la busqueda:")
        print(f"\n{verificar_registro}")

        res = input("\nSeguro que quiere eliminar? S/N: ").lower()

    except json.JSONDecodeError:
        print(
            "El archivo no se encontró o hay otro error al momento de buscar el usuario. Intente de nuevo"
        )
        eliminar_us()
    except ValueError:
        print("Algún valor fue ingresado incorrectamente. Intente de nuevo.")
        eliminar_us()
    except Exception as e:
        print(f"Error inesperado: {e}. Intente de nuevo.")
        eliminar_us()

    if res == "s":
        with open(
            os.path.join(DATA_DIR, "residente_r.json"), "w", encoding="utf-8"
        ) as h:
            json.dump(registro_actualizado, h, indent=4)

        with open(
            os.path.join(DATA_DIR, "contraseñas_residente.json"), "w", encoding="utf-8"
        ) as i:
            json.dump(contra_actualizada, i, indent=4)

        anotar_evento("ELIMINACIÓN", "Usuario eliminado del sistema.", user)
        print("Usuario eliminado correctamente.")

    elif res == "n":
        print("Operación cancelada. Volviendo al menú.")
        menus.menu_admin()


def cambiar_info():
    """Modifica la información de un usuario residente.

    Permite cambiar nombre, apellidos, teléfono o dirección
    de un usuario existente, actualizando ambos archivos JSON.
    """
    print("\n---------- CAMBIAR INFORMACIÓN DE USUARIO ----------")

    user = input("Ingrese el nombre del usuario: ")

    with open(os.path.join(DATA_DIR, "residente_r.json"), "r", encoding="utf-8") as f:
        lista = json.load(f)

    with open(
        os.path.join(DATA_DIR, "contraseñas_residente.json"), "r", encoding="utf-8"
    ) as h:
        lista_contra = json.load(h)

    cambio = next((item for item in lista if item["Nombres"] == user), None)
    cambio_contra = next(
        (items for items in lista_contra if items["Nombres"] == user), None
    )

    if cambio is None:
        print("Usuario no encontrado.")
        menus.menu_admin()
        return

    print(f"Ingrese la información que quiere cambiar de {user}.")
    dic = {1: "Nombres", 2: "Apellidos", 3: "Telefono", 4: "Dirección"}
    print(dic)

    res = int(input("Ingrese una opción (1-4): "))

    if res == 1:
        _cambiar_campo(user, lista, lista_contra, cambio, cambio_contra, "Nombres")
    elif res == 2:
        _cambiar_campo(user, lista, lista_contra, cambio, cambio_contra, "Apellidos")
    elif res == 3:
        _cambiar_campo(user, lista, lista_contra, cambio, cambio_contra, "Telefono")
    elif res == 4:
        _cambiar_campo(user, lista, lista_contra, cambio, cambio_contra, "Dirección")


def _cambiar_campo(user, lista, lista_contra, cambio, cambio_contra, campo):
    """Cambia un campo específico de un usuario y guarda los cambios.

    Args:
        user: Nombre del usuario a modificar.
        lista: Lista de datos de residentes.
        lista_contra: Lista de credenciales de residentes.
        cambio: Diccionario del usuario en la lista de datos.
        cambio_contra: Diccionario del usuario en la lista de credenciales.
        campo: Nombre del campo a modificar.
    """
    try:
        nuevo_valor = input(f"Ingrese el nuevo {campo} del usuario: ")
        cambio[campo] = nuevo_valor
        cambio_contra[campo] = nuevo_valor

        resp = input("Guardar? S/N: ").lower()

        if resp == "s":
            with open(
                os.path.join(DATA_DIR, "residente_r.json"), "w", encoding="utf-8"
            ) as g:
                json.dump([lista], g, indent=4)

            with open(
                os.path.join(DATA_DIR, "contraseñas_residente.json"),
                "w",
                encoding="utf-8",
            ) as i:
                json.dump([lista_contra], i, indent=4)

            anotar_evento("MODIFICACIÓN", f"{campo} de usuario modificado.", nuevo_valor)
            print(f"{campo} cambiado correctamente.")
        elif resp == "n":
            print("Operación cancelada.")
        else:
            print("Valor ingresado inválido. Redirigiendo al menú.")
            menus.menu_admin()

    except ValueError:
        print("Algún valor ingresado es inválido. Redirigiendo al menú.")
        menus.menu_admin()
    except Exception as e:
        print(f"Error inesperado: {e}. Redirigiendo al menú.")
        menus.menu_admin()


def crear_us():
    """Registra un nuevo usuario residente en el sistema.

    Solicita los datos personales y una contraseña,
    y los guarda en los archivos JSON correspondientes.
    """
    print("\n--------- CREAR USUARIO ----------")

    nuevo_n = input("\nIngrese el/los nombre/s del usuario nuevo: ")
    nuevo_a = input("\nIngrese el/los apellido/s del usuario nuevo: ")
    nuevo_t = input("\nIngrese el teléfono del usuario nuevo: ")
    nuevo_d = input("\nIngrese la dirección del usuario nuevo: ")
    nuevo_c = input("\nIngrese una contraseña para el usuario: ")

    info = {
        "Nombres": nuevo_n,
        "Apellidos": nuevo_a,
        "Telefono": nuevo_t,
        "Dirección": nuevo_d,
        "Rol": "Residente",
    }

    info_contra = {"Nombres": nuevo_n, "Contraseña": nuevo_c}

    if os.path.exists(os.path.join(DATA_DIR, "residente_r.json")):
        with open(os.path.join(DATA_DIR, "residente_r.json"), "r", encoding="utf-8") as f:
            lista = json.load(f)
    else:
        lista = []

    lista.append(info)

    if os.path.exists(os.path.join(DATA_DIR, "contraseñas_residente.json")):
        with open(
            os.path.join(DATA_DIR, "contraseñas_residente.json"), "r", encoding="utf-8"
        ) as g:
            lista_contra = json.load(g)
    else:
        lista_contra = []

    lista_contra.append(info_contra)

    res = input("Desea guardar el nuevo usuario? S/N: ").lower()

    if res == "s":
        with open(
            os.path.join(DATA_DIR, "residente_r.json"), "w", encoding="utf-8"
        ) as e:
            json.dump(lista, e, indent=4)

        with open(
            os.path.join(DATA_DIR, "contraseñas_residente.json"), "w", encoding="utf-8"
        ) as r:
            json.dump(lista_contra, r, indent=4)

        anotar_evento("CREACIÓN", "Nuevo residente registrado.", nuevo_n)
        print("\nUsuario guardado correctamente.")
        menus.menu_admin()


def listar():
    """Muestra todos los usuarios residentes registrados."""
    if os.path.exists(os.path.join(DATA_DIR, "residente_r.json")):
        with open(os.path.join(DATA_DIR, "residente_r.json"), "r", encoding="utf-8") as f:
            listas = json.load(f)
            print(listas)
    else:
        print("Archivo no encontrado. No hay usuarios registrados.")


def menu_gestion_us():
    """Muestra el menú de gestión de usuarios."""
    print("\n--------- MENU DE GENTIÓN DE USUARIO ---------")
    print("\n1. Crear usuario.")
    print("\n2. Cambiar información de un usuario.")
    print("\n3. Listar usuario.")
    print("\n4. Borrar usuario.")
    print("\n0. Volver al menú principal.")

    res = int(input("\nElija una opción: "))

    if res == 1:
        crear_us()
    elif res == 2:
        cambiar_info()
    elif res == 3:
        listar()
        menu_gestion_us()
    elif res == 4:
        eliminar_us()
    elif res == 0:
        menus.menu_admin()
