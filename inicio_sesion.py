import sesion_logica
import json
import os
import menus
import sys

def inicio_sesion():

        try:
            print("\n---------- INICIO DE SESIÓN ----------")

            print("\nIniciar sesión como:")
            print("\n1. Administrador.")
            print("\n2. Residente")
            print("\n0. Salir del programa.")
            res = int(input("\nIngrese una opción (1, 2): "))

            if res == 1:

                try:
                    if os.path.exists("contraseñas_admin.json"):
                        with open("contraseñas_admin.json", "r", encoding="utf-8") as f:
                            datos = json.load(f)
                    else:
                        print("\n-------------------------------------------")
                        print("\nEl archivo aún no se ha creado. Registrese.")
                        sesion_logica.registro_usuario()
                        with open("contraseñas_admin.json", "r", encoding="utf-8") as f:
                            datos = json.load(f)

                    print("\n---------- INICIO DE SESIÓN ADMIN ----------")

                    user = input("\nIngrese el/los nombre/s que registró en el programa: ")
                    contra = input("\nIngrese la contraseña registrada: ")

                    comprobante_user = next((item for item in datos if item["Nombres"] == user), None)
                    
                    if comprobante_user is None:
                        print("Usuario no encontrado.")
                        return
                    
                    confirmar = comprobante_user["Contraseña"]


                    if contra == confirmar:
                        print("\nInicio de sesión correcto.")
                        menus.menu_admin()
                    else:
                        print("\nUsuario o contraseña incorrecto. Intente de nuevo.")
                        inicio_sesion
                    
                except TypeError:
                    print("Algún valor fue ingresado incorrectamente. Intente de nuevo.")
                    inicio_sesion()
                except ValueError:
                    print("Algún valor fue ingresado incorrectamente. Intente de nuevo.")
                    inicio_sesion()

            elif res == 2:

                try :

                    if os.path.exists("contraseñas_residente.json"):
                        with open("contraseñas_residente.json", "r", encoding="utf-8") as f:
                            datos = json.load(f)
                    else:
                        print("\n-------------------------------------------")
                        print("\nEl archivo aún no se ha creado. Registrese.")
                        sesion_logica.registro_usuario()
                        with open("contraseñas_residente.json", "r", encoding="utf-8") as f:
                            datos = json.load(f)

                    print("\n---------- INICIO DE SESIÓN RESIDENTE ---------")
                    user = input("\nIngrese el/los nombre/s que registró en el programa: ")
                    contra = input("\nIngrese la contraseña registrada: ")
                    comprobante_user = next((item for item in datos if item["Nombres"] == user), None)
                    confirmar = comprobante_user["Contraseña"]
                    if contra == confirmar:
                        print("\nInicio de sesión correcto.")
                        menus.menu_residente()
                    else:
                        print("\nUsuario o contraseña incorrecto. Intente de nuevo.")
                        inicio_sesion()
                except TypeError:
                    print("\nAlgún valor fue ingresado incorrectamente. Intente de nuevo.")
                    inicio_sesion()
                except ValueError:
                    print("\nAlgún valor fue ingresado incorrectamente. Intente de nuevo")
                    inicio_sesion()
            elif res == 0:
                print("Saliendo del programa...")
                sys.exit()
            else:
                print("No se escribió algún valor válido. Intente de nuevo.")
                inicio_sesion()
        except ValueError:
            print("\nAlgún valor esta mal ingresado. Intente de nuevo.")
            inicio_sesion()
        
if __name__ == "__main__":
    inicio_sesion()