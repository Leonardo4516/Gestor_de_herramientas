# Sistema de Gestión de Herramientas y Préstamos

Sistema de consola en **Python** para administrar inventario de herramientas, registro de usuarios y control de préstamos en una comunidad o taller.

## Estructura del Proyecto

```
├── main.py                  # Punto de entrada principal
├── src/                     # Módulos de lógica
│   ├── __init__.py          # Inicializador del paquete
│   ├── inicio_sesion.py     # Autenticación de usuarios
│   ├── sesion_logica.py     # Registro de nuevos usuarios
│   ├── menus.py             # Menús de navegación por rol
│   ├── gestion_herramientas.py  # CRUD de herramientas
│   ├── gestion_usuarios.py  # CRUD de usuarios residentes
│   ├── prestamos_admin.py   # Gestión de préstamos (admin)
│   ├── prestamos_user.py    # Interfaz de préstamos (residente)
│   ├── logs.py              # Registro de eventos y respaldos
│   └── consulta_herramientas.py  # (en desuso)
├── data/                    # Archivos de persistencia
│   ├── herramientas.json
│   ├── prestamos.json
│   ├── admin_r.json
│   ├── residente_r.json
│   ├── contraseñas_admin.json
│   └── contraseñas_residente.json
└── registros/               # Archivos de log
    └── eventos.log
```

## Requisitos y Ejecución

1. Python 3.x instalado.
2. Ejecutar desde la raíz del proyecto:

```bash
python main.py
```

## Funcionalidades por Rol

### Administrador
- **Gestión de inventario**: Crear, listar, buscar, actualizar y eliminar herramientas con ID automático, cantidad, categoría y estado.
- **Control de usuarios**: Crear, modificar y eliminar residentes.
- **Supervisión de préstamos**: Registrar préstamos con verificación de stock, gestionar devoluciones y listar historial.
- **Seguridad**: Clave especial (`456`) para registro de cuenta administrativa.

### Residente
- **Consultas**: Listar herramientas disponibles.
- **Autogestión**: Solicitar préstamos y devoluciones.

## Persistencia de Datos

Los datos se almacenan en archivos **JSON** dentro del directorio `data/`:

| Archivo | Contenido |
|---|---|
| `herramientas.json` | Catálogo y stock de herramientas |
| `prestamos.json` | Historial de préstamos |
| `residente_r.json` | Perfiles de residentes |
| `admin_r.json` | Perfiles de administradores |
| `contraseñas_residente.json` | Credenciales de residentes |
| `contraseñas_admin.json` | Credenciales de administradores |

Los eventos del sistema se registran en `registros/eventos.log`.

## Notas Técnicas

- **Validaciones**: Bloques `try-except` para manejo de errores de entrada y archivos.
- **ID automático**: Herramientas y préstamos generan IDs incrementales.
- **Modularidad**: Separación en módulos dentro del paquete `src/`.
- **Logging**: Registro de eventos con funciones de respaldo y consulta.
