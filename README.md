
# Aplicación de Gestión de Proyectos

Esta es una aplicación web de gestión de proyectos construida con Flask y MySQL. Permite a los usuarios gestionar proyectos, empleados y asignaciones. La aplicación soporta operaciones CRUD para proyectos, empleados y asignaciones.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)

## Instalación

Para obtener una copia local y ponerla en funcionamiento, sigue estos sencillos pasos.

### Requisitos

- Python 3.x
- MySQL

### Clona el repositorio

```bash
git clone https://github.com/LuisRoft/gestion-proyectos
cd proyecto-app
```

### Crea un entorno virtual

```bash
python -m venv venv
```

### Activa el entorno virtual
Para Windows:

```bash
venv\Scripts\activate
```

Para macOS y Linux:

```bash
source venv/bin/activate
```

### Instala las dependencias

```bash
pip install -r requirements.txt
```

### Configura la base de datos
1. Abre `app.py` y actualiza las credenciales de la base de datos:

```python
app.config['MYSQL_HOST'] = 'tu_host'
app.config['MYSQL_USER'] = 'tu_usuario'
app.config['MYSQL_PASSWORD'] = 'tu_contraseña'
app.config['MYSQL_DB'] = 'proyectos'
```

2. El esquema de la base de datos se proporciona en el archivo `proyectos.sql`. Este archivo incluye las tablas necesarias y algunos datos iniciales.

### Ejecuta la aplicación

```bash
python app.py
```

## Uso

La aplicación tiene las siguientes funcionalidades principales:

- **Gestionar Proyectos**: Añadir, editar y eliminar proyectos.
- **Gestionar Empleados**: Añadir, editar y eliminar empleados.
- **Gestionar Asignaciones**: Asignar empleados a proyectos, editar y eliminar asignaciones.

### Tablas:

#### Proyectos
- `id`: Identificador único del proyecto.
- `nombre`: Nombre del proyecto.
- `descripcion`: Descripción del proyecto.
- `fecha_inicio`: Fecha de inicio del proyecto.
- `fecha_fin`: Fecha de fin del proyecto.

#### Empleados
- `id`: Identificador único del empleado.
- `nombre`: Nombre del empleado.
- `email`: Email del empleado.

#### Asignaciones
- `id`: Identificador único de la asignación.
- `proyecto_id`: Identificador del proyecto asignado.
- `empleado_id`: Identificador del empleado asignado.
- `fecha_asignacion`: Fecha de asignación del empleado al proyecto.

---