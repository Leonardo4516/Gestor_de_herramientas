"""Módulo de lógica de registro de usuarios.

Gestiona el registro inicial de administradores y residentes,
almacenando sus datos personales y credenciales en archivos JSON.
"""

import json
import os
from .logs import anotar_evento

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def registro_usuario():
    """Registra un nuevo usuario en el sistema.

    Solicita datos personales, el tipo de usuario (admin/residente),
    y en el caso de administradores valida una clave especial antes
    de completar el registro. Guarda la información y la contraseña
    en archivos JSON separados.
    """
    clave_pre = 456

    print("\n---------- REGISTRO ----------")

    try:
        nombres = input("\nIngrese sus nombres si aplica: ").capitalize()
        apellidos = input("\nIngrese sus apellidos si aplica: ").capitalize()
        telefono = int(input("\nIngrese su número de teléfono: "))
        direccion = input("\nIngrese su dirección de residencia: ")
        print("\nIngrese el rol de usuario:")
        print("\n1. Admin.")
        print("\n2. Residente.\n")
        tipo = int(input("Ingrese una opción entre 1 y 2: \n"))

    except TypeError:
        print("El valor ingresado no corresponde. Intente de nuevo.")
        registro_usuario()
    except ValueError:
        print("El valor ingresado no corresponde. Intente de nuevo.")
        registro_usuario()
    except KeyboardInterrupt:
        print("Salida forzada. Cerrando proceso...")
    except json.JSONDecodeError:
        print("Problemas con el archivo .JSON.")
    except Exception as e:
        print(f"Hay un error inesperado: {e}")

    info = {
        "Nombres": nombres,
        "Apellidos": apellidos,
        "Teléfono": telefono,
        "Dirección": direccion,
    }

    admin_l = []
    residente_l = []
    contra_admin_l = []
    contra_residente_l = []

    if tipo == 1:
        clave_ver = int(input("Ingrese la clave para la creación de cuenta de administrador: "))

        if clave_ver == clave_pre:
            info["Rol"] = "Admin"

            if os.path.exists(os.path.join(DATA_DIR, "admin_r.json")):
                with open(os.path.join(DATA_DIR, "admin_r.json"), "r", encoding="utf-8") as f:
                    admin_l = json.load(f)
            else:
                admin_l = []

            admin_l.append(info)

            with open(os.path.join(DATA_DIR, "admin_r.json"), "w", encoding="utf-8") as f:
                json.dump(admin_l, f, indent=4)

            print("La clave es correcta. Ahora cree una contraseña.")

            contraseña_admin = input("Ingrese una contraseña: ")

            contra_admin_dic = {
                "Nombres": nombres,
                "Contraseña": contraseña_admin,
            }

            if os.path.exists(os.path.join(DATA_DIR, "contraseñas_admin.json")):
                with open(os.path.join(DATA_DIR, "contraseñas_admin.json"), "r", encoding="utf-8") as f:
                    contra_admin_l = json.load(f)
            else:
                contra_admin_l = []

            contra_admin_l.append(contra_admin_dic)

            with open(os.path.join(DATA_DIR, "contraseñas_admin.json"), "w", encoding="utf-8") as f:
                json.dump(contra_admin_l, f, indent=4)

            anotar_evento("REGISTRO", "Nuevo administrador registrado.", nombres)
            print("Registro realizado con éxito.")
        else:
            print("La clave de creación es incorrecta. Vuelva a registrarse.")
            registro_usuario()

    elif tipo == 2:
        info["Rol"] = "Residente"

        if os.path.exists(os.path.join(DATA_DIR, "residente_r.json")):
            with open(os.path.join(DATA_DIR, "residente_r.json"), "r", encoding="utf-8") as f:
                residente_l = json.load(f)
        else:
            residente_l = []

        residente_l.append(info)

        with open(os.path.join(DATA_DIR, "residente_r.json"), "w", encoding="utf-8") as f:
            json.dump(residente_l, f, indent=4)

        print("Ahora cree una contraseña.")
        contraseña_residente = input("\nIngrese una contraseña: ")

        contra_residente_dic = {
            "Nombres": nombres,
            "Contraseña": contraseña_residente,
        }

        if os.path.exists(os.path.join(DATA_DIR, "contraseñas_residente.json")):
            with open(os.path.join(DATA_DIR, "contraseñas_residente.json"), "r", encoding="utf-8") as f:
                contra_residente_l = json.load(f)
        else:
            contra_residente_l = []

        contra_residente_l.append(contra_residente_dic)

        with open(os.path.join(DATA_DIR, "contraseñas_residente.json"), "w", encoding="utf-8") as f:
            json.dump(contra_residente_l, f, indent=4)

        anotar_evento("REGISTRO", "Nuevo residente registrado.", nombres)
        print("Registro realizado con éxito.")

    else:
        print("No ingresó un valor válido. Intente de nuevo")
        registro_usuario()