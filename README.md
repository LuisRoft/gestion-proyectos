# Aplicación de Gestión de Inventarios

Esta es una aplicación web de gestión de inventarios construida con Flask y MySQL. Permite a los usuarios gestionar productos, proveedores y compras. La aplicación soporta operaciones CRUD para productos, proveedores y compras.

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
git clone https://github.com/LuisRoft/inventario-app.git
cd inventario-app
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
1. Abre app.py y actualiza las credenciales de la base de datos:

```bash
app.config['MYSQL_HOST'] = 'tu_host'
app.config['MYSQL_USER'] = 'tu_usuario'
app.config['MYSQL_PASSWORD'] = 'tu_contraseña'
app.config['MYSQL_DB'] = 'inventario'
```

2. El esquema de la base de datos se proporciona en el archivo inventario.sql. Este archivo incluye las tablas necesarias y algunos datos iniciales.


### Ejecuta la aplicacion

```bash
python app.py
```

### Uso
La aplicación tiene las siguientes funcionalidades principales:

- Gestionar Productos: Añadir, editar y eliminar productos.
- Gestionar Proveedores: Añadir, editar y eliminar proveedores.
- Gestionar Compras: Añadir, editar y eliminar compras.
