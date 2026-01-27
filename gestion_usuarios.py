import json
import os
import menus
import prestamos_admin
from logs import anotar_evento

def eliminar_us():

    print("\n---------- ELIMINAR USUARIO ----------")

    try:   
        reg_el = []

        contra_el = []

        with open("residente_r.json", "r", encoding="utf-8") as f:
            reg_el = json.load(f)

        with open("contraseñas_residente.json", "r", encoding="utf-8") as e:
            contra_el = json.load(e)

        user = input("Ingrese el nombre del usuario: ")

        registro_actualizado = []
        contra_actualizada = []

        for registro_actualizado_a in reg_el:
            if registro_actualizado_a["Nombres"] != user:
                registro_actualizado.append(registro_actualizado_a)

        for contra_actualizada_a in contra_el:
            if contra_actualizada_a["Nombres"] != user:
                contra_actualizada.append(contra_actualizada_a)

        #registro_actualizado = dict(next((itemsa for itemsa in reg_el if itemsa["Nombres"] != user), None))
        #contra_actualizada = next((item for item in contra_el if item["Nombres"] != user), None)
        verificar_registro = next((items_v for items_v in reg_el if items_v["Nombres"] == user), None)

        print("\nInformación encontrada en base a la busqueda:")
        print(f"\n{verificar_registro}")


        res = input("\nSeguro que quiere eliminar? S/N: ").lower()
    except json.JSONDecodeError:
        print("El archivo no se encontró o hay otro error al momento de buscar el usuario. Intente de nuevo")
        eliminar_us()
    except ValueError:
        print("Algún valor fue ingresado incorrectamente. Intente de nuevo.")
        eliminar_us()
    except Exception as e:
        print(f"Error inesperado: {e}. Intente de nuevo.")
        eliminar_us()

    if res == "s":

        with open("residente_r.json", "w", encoding="utf-8") as h:
            json.dump(registro_actualizado, h, indent=4)

        with open("contraseñas_residente.json", "w", encoding="utf-8") as i:
            json.dump(contra_actualizada, i, indent=4)

        anotar_evento("ELIMINACIÓN", "Usuario eliminado del sistema.", user)

        print("Usuario eliminado correctamente.")
    elif res == "n":
        print("Operación cancelada. Volviendo al menú.")
        menus.menu_admin()

def cambiar_info():

    print("\n---------- CAMBIAR INFORMACIÓN DE USUARIO ----------")

    user = input("Ingrese el nombre del usuario: ")

    lista = []
    lista_contra = []

    with open("residente_r.json", "r", encoding="utf-8") as f:
        lista = json.load(f)

    with open("contraseñas_residente.json", "r", encoding="utf-8") as h:
        lista_contra = json.load(h)

    cambio = next((item for item in lista if item["Nombres"] == user), None)
    cambio_contra = next((items for items in lista_contra if items["Nombres"] == user), None)

    print(f"Ingrese la información que quiere cambiar de {user}.")
    dic = {
        1 : "Nombres",
        2 : "Apellidos",
        3 : "Telefono",
        4 : "Dirección",
    }
    print(dic)


    res = int(input("Ingrese una opción (1-4): "))

    if res == 1:
        def cambiar_nombre():
            try:
                nombre_n = input("Ingrese el nuevo nombre del usuario: ")
                cambio["Nombres"] = nombre_n
                cambio_contra["Nombres"] = nombre_n

                asd = []
                asd_contra = []
                asd.append(lista)
                asd_contra.append(lista_contra)

                resp = input("Guardar? S/N: ").lower()
                if resp == "s":
                    with open("residente_r.json", "w", encoding="utf-8") as g:
                        json.dump(asd, g, indent=4)

                    with open("contraseñas_residente.json", "w", encoding="utf-8") as i:
                        json.dump(asd_contra, i, indent=4)
                elif resp == "n":
                    print("Volviendo a iniciar.")
                    cambiar_nombre()
                else:
                    print("Valor ingresado inválido. Redirigiendo al menú.")
                    menus.menu_admin()
            except ValueError:
                print("Algún valor ingresado es inválido. Redirigiendo al menú.")
                menus.menu_admin()
            except Exception as e:
                print(f"Error inesperado: {e}. Redirigiendo al menú.")
                menus.menu_admin()

            anotar_evento("MODIFICACIÓN", "Nombre de usuario modificado.", nombre_n)
        cambiar_nombre()

    elif res == 2:
        def cambiar_apellidos():
            try:
                apellido_n = input("Ingrese el/los nuevo/s apellido/s del usuario: ")
                cambio["Apellidos"] = apellido_n
                cambio_contra["Apellidos"] = apellido_n

                asd = []
                asd_contra = []
                asd.append(lista)
                asd_contra.append(lista_contra)

                resp = input("Guardar? S/N: ").lower()
                if resp == "s":
                    with open("residente_r.json", "w", encoding="utf-8") as g:
                        json.dump(asd, g, indent=4)

                    with open("contraseñas_residente.json", "w", encoding="utf-8") as i:
                        json.dump(asd_contra, i, indent=4)
                elif resp == "n":
                    print("Volviendo a iniciar.")
                    cambiar_apellidos()
                else:
                    print("Valor ingresado inválido. Redirigiendo al menú.")
                    menus.menu_admin()
            except ValueError:
                print("Algún valor ingresado es inválido. Redirigiendo al menú.")
                menus.menu_admin()
            except Exception as e:
                print(f"Error inesperado: {e}. Redirigiendo al menú.")
                menus.menu_admin()
            
            anotar_evento("MODIFICACIÓN", "Apellidos de usuario modificado.", apellido_n)

            print("Apellidos cambiados correctamente.")

        cambiar_apellidos()
    elif res == 3:
        def cambiar_telefono():
            try:
                telefono_n = input("Ingrese el/los nuevo/s apellido/s del usuario: ")
                cambio["Telefono"] = telefono_n
                cambio_contra["Telefono"] = telefono_n

                asd = []
                asd_contra = []
                asd.append(lista)
                asd_contra.append(lista_contra)

                resp = input("Guardar? S/N: ").lower()
                if resp == "s":
                    with open("residente_r.json", "w", encoding="utf-8") as g:
                        json.dump(asd, g, indent=4)

                    with open("contraseñas_residente.json", "w", encoding="utf-8") as i:
                        json.dump(asd_contra, i, indent=4)
                elif resp == "n":
                    print("Volviendo a iniciar.")
                    cambiar_telefono()
                else:
                    print("Valor ingresado inválido. Redirigiendo al menú.")
                    menus.menu_admin()
            except ValueError:
                print("Algún valor ingresado es inválido. Redirigiendo al menú.")
                menus.menu_admin()
            except Exception as e:
                print(f"Error inesperado: {e}. Redirigiendo al menú.")
                menus.menu_admin()

            anotar_evento("MODIFICACIÓN", "Teléfono de usuario modificado.", telefono_n)

            print("Teléfono cambiado correctamente.")
            
            cambiar_telefono()
            
    elif res == 4:
        def cambiar_direccion():
            try:
                apellido_n = input("Ingrese el/los nuevo/s apellido/s del usuario: ")
                cambio["Dirección"] = apellido_n
                cambio_contra["Dirección"] = apellido_n

                asd = []
                asd_contra = []
                asd.append(lista)
                asd_contra.append(lista_contra)

                resp = input("Guardar? S/N: ").lower()
                if resp == "s":
                    with open("residente_r.json", "w", encoding="utf-8") as g:
                        json.dump(asd, g, indent=4)

                    with open("contraseñas_residente.json", "w", encoding="utf-8") as i:
                        json.dump(asd_contra, i, indent=4)
                elif resp == "n":
                    print("Volviendo a iniciar.")
                    cambiar_direccion()
                else:
                    print("Valor ingresado inválido. Redirigiendo al menú.")
                    menus.menu_admin()
            except ValueError:
                print("Algún valor ingresado es inválido. Redirigiendo al menú.")
                menus.menu_admin()
            except Exception as e:
                print(f"Error inesperado: {e}. Redirigiendo al menú.")
                menus.menu_admin()

            anotar_evento("MODIFICACIÓN", "Dirección de usuario modificado.", apellido_n)

            print("Dirección cambiada correctamente.")

        cambiar_direccion()

def crear_us():

    print("\n--------- CREAR USUARIO ----------")

    nuevo_n = input("\nIngrese el/los nombre/s del usuario nuevo: ")
    nuevo_a = input("\nIngrese el/los apellido/s del usuario nuevo: ")
    nuevo_t = input("\nIngrese el teléfono del usuario nuevo: ")
    nuevo_d = input("\nIngrese la dirección del usuario nuevo: ")
    nuevo_c = input("\nIngrese una contraseña para el usuario: ")

    
    info = {
            "Nombres" : nuevo_n,
            "Apellidos" : nuevo_a,
            "Telefono" : nuevo_t,
            "Dirección" : nuevo_d,
            "Rol" : "Residente"
        }
    
    info_contra = {
        "Nombres" : nuevo_n,
        "Contraseña" : nuevo_c
    }
    
    if os.path.exists("residente_r.json"):
        with open("residente_r.json", "r", encoding="utf-8") as f:
            lista = json.load(f)
    else:
        lista = []

    lista.append(info)

    
    if os.path.exists("contraseñas_residente.json"):
        with open("contraseñas_residente.json", "r", encoding="utf-8") as g:
            lista_contra = json.load(g)
    else:
        lista_contra = []

    lista_contra.append(info_contra)

    

    res = input("Desea guardar el nuevo usuario? S/N: ").lower()

    if res == "s":
        
        with open("residente_r.json", "w", encoding="utf-8") as e:
            json.dump(lista, e, indent=4)

        with open("contraseñas_residente.json", "w", encoding="utf-8") as r:
            json.dump(lista_contra, r, indent=4)

        anotar_evento("CREACIÓN", "Nuevo residente registrado.", nuevo_n)

        print("\nUsuario guardado correctamente.")
        menus.menu_admin()

    

def listar():
    
    lista = []

    if os.path.exists("residente_r.json"):
        with open("residente_r.json", "r", encoding="utf-8") as f:
            listas = json.load(f)
            
            lista.append(listas)

            print(listas)
    else:
        print("Archivo no encontrado. No hay usuarios registrados.")
        

def menu_gestion_us():
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
    elif res == 4:
        eliminar_us()
    elif res == 0:
        menus.menu_admin()