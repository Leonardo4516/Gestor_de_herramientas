# 🛠️ Sistema de Gestión de Herramientas y Préstamos

Este sistema es una aplicación de consola desarrollada en **Python** diseñada para administrar el inventario de herramientas, el registro de usuarios y el control de préstamos de una comunidad o taller.

## 📋 Estructura de Módulos

El proyecto se organiza en los siguientes archivos interconectados:

* **`inicio_sesion.py`**: Punto de entrada principal que gestiona el acceso de administradores y residentes.
* **`menus.py`**: Define las interfaces de navegación para los diferentes roles del sistema.
* **`gestion_herramientas.py`**: Contiene la lógica para crear, listar, buscar, actualizar y eliminar herramientas.
* **`gestion_usuarios.py`**: Permite al administrador gestionar los datos de los residentes (cambio de info, eliminación y listado).
* **`prestamos_admin.py`**: Módulo central para registrar salidas de herramientas, devoluciones y ver el historial.
* **`prestamos_user.py`**: Interfaz simplificada para que los residentes soliciten y devuelvan herramientas.
* **`sesion_logica.py`**: Maneja el registro inicial de nuevos usuarios y la asignación de roles.

---

## 🚀 Requisitos y Ejecución

1.  **Instalación**: Asegúrate de tener instalado Python 3.x.
2.  **Archivos**: Todos los archivos `.py` deben estar en la misma carpeta raíz.
3.  **Ejecución**: Abre la terminal en Visual Studio Code y ejecuta:
    ```bash
    python inicio_sesion.py
    ```

---

## 🔑 Funcionalidades por Rol

### Administrador
* **Gestión de Inventario**: Puede añadir herramientas con ID automático, cantidad, categoría y estado.
* **Control de Usuarios**: Capacidad para modificar nombres, teléfonos o direcciones, y eliminar registros de la base de datos.
* **Supervisión de Préstamos**: Registra préstamos verificando el stock disponible y gestiona las devoluciones para restaurar el inventario.
* **Seguridad**: Requiere una clave especial (`456`) para el registro de cuenta administrativa.

### Residente
* **Consultas**: Puede listar las herramientas disponibles en el sistema.
* **Autogestión**: Puede registrar sus propios préstamos indicando la fecha estimada de devolución.

---

## 📂 Persistencia de Datos
El sistema utiliza archivos **JSON** para almacenar la información de manera local:
* `herramientas.json`: Almacena el catálogo y stock.
* `prestamos.json`: Guarda el historial de transacciones.
* `residente_r.json` / `admin_r.json`: Contiene los perfiles de usuario.
* `contraseñas_residente.json` / `contraseñas_admin.json`: Almacena las credenciales de acceso de forma separada.

---

## ⚠️ Notas Técnicas
* **Validaciones**: El código incluye bloques `try-except` para manejar errores de entrada de datos (ValueError) y archivos no encontrados.
* **ID Automático**: Las herramientas y préstamos generan sus identificadores de forma incremental basándose en los datos existentes.


# ARCHIVO MARKDOWN

https://drive.google.com/file/d/1MehqPAfHe536uin6slYMzkvEnEDlKb7e/view?usp=sharing