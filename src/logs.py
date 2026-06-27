"""Módulo de registro de eventos (logging).

Proporciona funciones para anotar, visualizar y respaldar
eventos del sistema en un archivo de texto plano.
"""

import os
from datetime import datetime

# Rutas de almacenamiento de registros
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETA_REGISTROS = os.path.join(BASE_DIR, "registros")
archivo_registros = os.path.join(CARPETA_REGISTROS, "eventos.log")

if not os.path.exists(CARPETA_REGISTROS):
    os.makedirs(CARPETA_REGISTROS)


def anotar_evento(tipo_accion, descripcion_evento, nombre_usuario=None):
    """Registra un evento en el archivo de logs.

    Args:
        tipo_accion: Categoría del evento (ej: "INICIO DE SESIÓN", "CREACIÓN").
        descripcion_evento: Texto descriptivo del evento ocurrido.
        nombre_usuario: Nombre del usuario involucrado (opcional).
    """
    try:
        momento = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        dato_usuario = f"Usuario: {nombre_usuario}" if nombre_usuario else ""
        texto_evento = f"[{momento}] [{tipo_accion}] {dato_usuario} | {descripcion_evento}\n"

        with open(archivo_registros, "a", encoding="utf-8") as f:
            f.write(texto_evento)

    except Exception as e:
        print(f"Error al guardar registro: {e}")


def ver_registros(maximo=50):
    """Muestra los últimos eventos registrados.

    Args:
        maximo: Cantidad máxima de líneas a mostrar (por defecto 50).
    """
    try:
        if not os.path.exists(archivo_registros):
            print("No hay eventos registrados aún.")
            return

        with open(archivo_registros, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        mostrar = lineas[-maximo:] if len(lineas) > maximo else lineas

        print("\n" + "-" * 100)
        print(" " * 40 + "REGISTRO DE EVENTOS")
        print("-" * 100)

        if mostrar:
            for linea in mostrar:
                print(linea.strip())
        else:
            print("No hay eventos registrados.")

        print("-" * 100)
        print(f"\nMostrando últimos {len(mostrar)} de {len(lineas)} eventos totales")

    except Exception as e:
        print(f"Error al leer registros: {e}")


def hacer_respaldo():
    """Crea un respaldo del archivo de registros y lo limpia."""
    try:
        if os.path.exists(archivo_registros):
            ahora = datetime.now().strftime("%Y%m%d_%H%M%S")
            ruta_respaldo = os.path.join(CARPETA_REGISTROS, f"eventos_backup_{ahora}.log")

            with open(archivo_registros, "r", encoding="utf-8") as original:
                contenido = original.read()

            with open(ruta_respaldo, "w", encoding="utf-8") as copia:
                copia.write(contenido)

            with open(archivo_registros, "w", encoding="utf-8") as f:
                f.write("")

            print(f"Respaldo creado: {ruta_respaldo}")
        else:
            print("No hay registros para respaldar.")

    except Exception as e:
        print(f"Error al crear respaldo: {e}")