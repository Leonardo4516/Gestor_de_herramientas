"""Módulo de inicio de sesión.

Maneja la autenticación de administradores y residentes,
verificando credenciales contra los archivos JSON de contraseñas.
"""

import json
import os
import sys
from . import sesion_logica, menus, logs

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def inicio_sesion():
    """Muestra el menú de inicio de sesión y autentica al usuario.

    Permite elegir entre inicio de sesión como administrador o residente.
    Verifica las credenciales contra los archivos de almacenamiento y
    redirige al menú correspondiente. Si no hay usuarios registrados,
    solicita un registro previo.
    """
    try:
        print("\n---------- INICIO DE SESIÓN ----------")
        print("\nIniciar sesión como:")
        print("\n1. Administrador.")
        print("\n2. Residente")
        print("\n0. Salir del programa.")
        res = int(input("\nIngrese una opción (1, 2): "))

        if res == 1:
            _autenticar_admin()
        elif res == 2:
            _autenticar_residente()
        elif res == 0:
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("No se escribió algún valor válido. Intente de nuevo.")
            inicio_sesion()

    except ValueError:
        print("\nAlgún valor esta mal ingresado. Intente de nuevo.")
        inicio_sesion()
    except TypeError:
        print("\nAlgún valor esta mal ingresado. Intente de nuevo.")
        inicio_sesion()
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        sys.exit()
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
        inicio_sesion()


def _autenticar_admin():
    """Autentica a un administrador contra el archivo de credenciales."""
    try:
        archivo_admin = os.path.join(DATA_DIR, "contraseñas_admin.json")

        if os.path.exists(archivo_admin):
            with open(archivo_admin, "r", encoding="utf-8") as f:
                datos = json.load(f)
        else:
            print("\n-------------------------------------------")
            print("\nEl archivo aún no se ha creado. Registrese.")
            sesion_logica.registro_usuario()
            with open(archivo_admin, "r", encoding="utf-8") as f:
                datos = json.load(f)

        print("\n---------- INICIO DE SESIÓN ADMIN ----------")
        user = input("\nIngrese el/los nombre/s que registró en el programa: ")
        contra = input("\nIngrese la contraseña registrada: ")

        comprobante_user = next(
            (item for item in datos if item["Nombres"] == user), None
        )

        if comprobante_user is None:
            print("Usuario no encontrado.")
            inicio_sesion()
            return

        if contra == comprobante_user["Contraseña"]:
            print("\nInicio de sesión correcto.")
            logs.anotar_evento(
                "INICIO DE SESIÓN", "Un administrador ha iniciado sesión.", user
            )
            menus.menu_admin()
        else:
            print("\nUsuario o contraseña incorrecto. Intente de nuevo.")
            logs.anotar_evento(
                "INICIO DE SESIÓN INCORRECTO",
                "Un admin ha tratado iniciado sesión.",
                user,
            )
            inicio_sesion()

    except TypeError:
        print("Algún valor fue ingresado incorrectamente. Intente de nuevo.")
        inicio_sesion()
    except ValueError:
        print("Algún valor fue ingresado incorrectamente. Intente de nuevo.")
        inicio_sesion()


def _autenticar_residente():
    """Autentica a un residente contra el archivo de credenciales."""
    try:
        archivo_residente = os.path.join(DATA_DIR, "contraseñas_residente.json")

        if os.path.exists(archivo_residente):
            with open(archivo_residente, "r", encoding="utf-8") as f:
                datos = json.load(f)
        else:
            print("\n-------------------------------------------")
            print("\nEl archivo aún no se ha creado. Registrese.")
            sesion_logica.registro_usuario()
            with open(archivo_residente, "r", encoding="utf-8") as f:
                datos = json.load(f)

        print("\n---------- INICIO DE SESIÓN RESIDENTE ---------")
        user = input("\nIngrese el/los nombre/s que registró en el programa: ")
        contra = input("\nIngrese la contraseña registrada: ")

        comprobante_user = next(
            (item for item in datos if item["Nombres"] == user), None
        )

        if comprobante_user is None:
            print("Usuario no encontrado.")
            inicio_sesion()
            return

        if contra == comprobante_user["Contraseña"]:
            print("\nInicio de sesión correcto.")
            logs.anotar_evento(
                "INICIO DE SESIÓN", "Un usuario ha iniciado sesión.", user
            )
            menus.menu_residente()
        else:
            print("\nUsuario o contraseña incorrecto. Intente de nuevo.")
            logs.anotar_evento(
                "INICIO DE SESIÓN INCORRECTO",
                "Un usuario ha tratado iniciado sesión.",
                user,
            )
            inicio_sesion()

    except TypeError:
        print("\nAlgún valor fue ingresado incorrectamente. Intente de nuevo.")
        inicio_sesion()
    except ValueError:
        print("\nAlgún valor fue ingresado incorrectamente. Intente de nuevo")
        inicio_sesion()


if __name__ == "__main__":
    inicio_sesion()