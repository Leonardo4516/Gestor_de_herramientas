import os
from datetime import datetime

# Carpeta donde se guardarán los registros
CARPETA_REGISTROS = "registros"
archivo_registros = os.path.join(CARPETA_REGISTROS, "eventos.log")

# Asegurar que la carpeta exista
if not os.path.exists(CARPETA_REGISTROS):
    os.makedirs(CARPETA_REGISTROS)


def anotar_evento(tipo_accion, descripcion_evento, nombre_usuario=None):
    """Guarda un evento en el archivo de registros"""
    try:
        momento = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        if nombre_usuario:
            dato_usuario = f"Usuario: {nombre_usuario}"
        else:
            dato_usuario = ""
        
        texto_evento = f"[{momento}] [{tipo_accion}] {dato_usuario} | {descripcion_evento}\n"
        
        with open(archivo_registros, "a", encoding="utf-8") as f:
            f.write(texto_evento)
            
    except Exception as e:
        print(f"Error al guardar registro: {e}")


def ver_registros(maximo=50):
    """Muestra los últimos registros del archivo"""
    try:
        if not os.path.exists(archivo_registros):
            print("No hay eventos registrados aún.")
            return
        
        with open(archivo_registros, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        
        # Mostrar las últimas 'maximo' líneas
        mostrar = lineas[-maximo:] if len(lineas) > maximo else lineas
        
        print("\n" + "-"*100)
        print(" " * 40 + "REGISTRO DE EVENTOS")
        print("-"*100)
        
        if mostrar:
            for linea in mostrar:
                print(linea.strip())
        else:
            print("No hay eventos registrados.")
        
        print("-"*100)
        print(f"\nMostrando últimos {len(mostrar)} de {len(lineas)} eventos totales")
        
    except Exception as e:
        print(f"Error al leer registros: {e}")


def hacer_respaldo():
    """Crea un respaldo del archivo de registros y lo limpia"""
    try:
        if os.path.exists(archivo_registros):
            # Crear nombre de respaldo
            ahora = datetime.now().strftime("%Y%m%d_%H%M%S")
            ruta_respaldo = os.path.join(CARPETA_REGISTROS, f"eventos_backup_{ahora}.log")
            
            # Copiar contenido al respaldo
            with open(archivo_registros, "r", encoding="utf-8") as original:
                contenido = original.read()
            
            with open(ruta_respaldo, "w", encoding="utf-8") as copia:
                copia.write(contenido)
            
            # Limpiar archivo original
            with open(archivo_registros, "w", encoding="utf-8") as f:
                f.write("")
            
            print(f"Respaldo creado: {ruta_respaldo}")
        else:
            print("No hay registros para respaldar.")
            
    except Exception as e:
        print(f"Error al crear respaldo: {e}")