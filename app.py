from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = '123456'

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'inventario'

mysql = MySQL(app)

@app.route('/')
def index_compras():
    cur = mysql.connection.cursor()
    cur.execute("SELECT c.id, p.nombre as producto_nombre, pr.nombre as proveedor_nombre, c.cantidad, c.fecha "
                "FROM compras c "
                "JOIN productos p ON c.id_producto = p.id "
                "JOIN proveedores pr ON c.id_proveedor = pr.id")
    compras = cur.fetchall()

    cur.execute("SELECT id, nombre FROM productos")
    productos = cur.fetchall()

    cur.execute("SELECT id, nombre FROM proveedores")
    proveedores = cur.fetchall()

    cur.close()
    return render_template('index_compras.html', compras=compras, productos=productos, proveedores=proveedores)

# Ruta para la página principal de productos
@app.route('/productos')
def index_productos():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM productos")
    if result_value > 0:
        productos = cur.fetchall()
        return render_template('index_productos.html', productos=productos)
    return render_template('index_productos.html')

# Ruta para la página principal de proveedores
@app.route('/proveedores')
def index_proveedores():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM proveedores")
    if result_value > 0:
        proveedores = cur.fetchall()
        return render_template('index_proveedores.html', proveedores=proveedores)
    return render_template('index_proveedores.html')

# Ruta para agregar un producto
@app.route('/add_producto', methods=['GET', 'POST'])
def add_producto():
    if request.method == 'POST':
        product_details = request.form
        nombre = product_details['nombre']
        descripcion = product_details['descripcion']
        precio = product_details['precio']
        stock = product_details['stock']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)", (nombre, descripcion, precio, stock))
        mysql.connection.commit()
        cur.close()
        flash('Producto agregado satisfactoriamente')
        return redirect(url_for('index_productos'))
    return render_template('add_producto.html')

@app.route('/add_proveedor', methods=['GET', 'POST'])
def add_proveedor():
    if request.method == 'POST':
        provider_details = request.form
        nombre = provider_details['nombre']
        contacto = provider_details['contacto']
        telefono = provider_details['telefono']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO proveedores (nombre, contacto, telefono) VALUES (%s, %s, %s)", (nombre, contacto, telefono))
        mysql.connection.commit()
        cur.close()
        flash('Proveedor agregado satisfactoriamente')
        return redirect(url_for('index_proveedores'))
    return render_template('add_proveedor.html')


# Ruta para editar un producto
@app.route('/edit_producto/<int:id>', methods=['GET', 'POST'])
def edit_producto(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM productos WHERE id = %s", [id])
    producto = cur.fetchone()
    if request.method == 'POST':
        product_details = request.form
        nombre = product_details['nombre']
        descripcion = product_details['descripcion']
        precio = product_details['precio']
        stock = product_details['stock']

        cur.execute("UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, stock = %s WHERE id = %s", (nombre, descripcion, precio, stock, id))
        mysql.connection.commit()
        cur.close()
        flash('Producto actualizado satisfactoriamente')
        return redirect(url_for('index_productos'))
    return render_template('edit_producto.html', producto=producto)

# Ruta para editar un proveedor
@app.route('/edit_proveedor/<int:id>', methods=['GET', 'POST'])
def edit_proveedor(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM proveedores WHERE id = %s", [id])
    proveedor = cur.fetchone()
    if request.method == 'POST':
        provider_details = request.form
        nombre = provider_details['nombre']
        contacto = provider_details['contacto']
        telefono = provider_details['telefono']

        cur.execute("UPDATE proveedores SET nombre = %s, contacto = %s, telefono = %s WHERE id = %s", (nombre, contacto, telefono, id))
        mysql.connection.commit()
        cur.close()
        flash('Proveedor actualizado satisfactoriamente')
        return redirect(url_for('index_proveedores'))
    return render_template('edit_proveedor.html', proveedor=proveedor)

# Ruta para eliminar un producto
@app.route('/delete_producto/<int:id>', methods=['POST'])
def delete_producto(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM productos WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Producto eliminado satisfactoriamente')
    return redirect(url_for('index_productos'))

# Ruta para eliminar un proveedor
@app.route('/delete_proveedor/<int:id>', methods=['POST'])
def delete_proveedor(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM proveedores WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Proveedor eliminado satisfactoriamente')
    return redirect(url_for('index_proveedores'))


# Ruta para agregar una compra
@app.route('/add_compra', methods=['GET', 'POST'])
def add_compra():
    if request.method == 'POST':
        compra_details = request.form
        id_producto = compra_details['id_producto']
        id_proveedor = compra_details['id_proveedor']
        cantidad = compra_details['cantidad']
        fecha = compra_details['fecha']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO compras (id_producto, id_proveedor, cantidad, fecha) VALUES (%s, %s, %s, %s)", (id_producto, id_proveedor, cantidad, fecha))
        mysql.connection.commit()
        cur.close()
        flash('Compra agregada satisfactoriamente')
        return redirect(url_for('index_compras'))
    return render_template('add_compra.html')

# Ruta para editar una compra
@app.route('/edit_compra/<int:id>', methods=['GET', 'POST'])
def edit_compra(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM compras WHERE id = %s", [id])
    compra = cur.fetchone()

    cur.execute("SELECT id, nombre FROM productos")
    productos = cur.fetchall()

    cur.execute("SELECT id, nombre FROM proveedores")
    proveedores = cur.fetchall()

    if request.method == 'POST':
        compra_details = request.form
        id_producto = compra_details['id_producto']
        id_proveedor = compra_details['id_proveedor']
        cantidad = compra_details['cantidad']
        fecha = compra_details['fecha']

        cur.execute("UPDATE compras SET id_producto = %s, id_proveedor = %s, cantidad = %s, fecha = %s WHERE id = %s", (id_producto, id_proveedor, cantidad, fecha, id))
        mysql.connection.commit()
        cur.close()
        flash('Compra actualizada satisfactoriamente')
        return redirect(url_for('index_compras'))
    return render_template('edit_compra.html', compra=compra, productos=productos, proveedores=proveedores)

# Ruta para eliminar una compra
@app.route('/delete_compra/<int:id>', methods=['POST'])
def delete_compra(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM compras WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Compra eliminada satisfactoriamente')
    return redirect(url_for('index_compras'))

if __name__ == '__main__':
    app.run(debug=True)
