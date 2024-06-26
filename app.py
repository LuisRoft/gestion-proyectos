from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = '123456'

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'bqevucf5pnlsxxqovja3-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'uktdesa4npr5ivsx'
app.config['MYSQL_PASSWORD'] = 'id1nrmXpthU2tCgLzoST'
app.config['MYSQL_DB'] = 'bqevucf5pnlsxxqovja3'

mysql = MySQL(app)

@app.route('/')
def index_proyectos():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM Proyectos")
    if result_value > 0:
        proyectos = cur.fetchall()
        return render_template('index_proyectos.html', proyectos=proyectos)
    return render_template('index_proyectos.html')


@app.route('/asignaciones')
def index_asignaciones():
    cur = mysql.connection.cursor()
    cur.execute("SELECT a.id, p.nombre as proyecto_nombre, e.nombre as empleado_nombre, a.fecha_asignacion "
                "FROM Asignaciones a "
                "JOIN Proyectos p ON a.proyecto_id = p.id "
                "JOIN Empleados e ON a.empleado_id = e.id")
    asignaciones = cur.fetchall()

    cur.execute("SELECT id, nombre FROM Proyectos")
    proyectos = cur.fetchall()

    cur.execute("SELECT id, nombre FROM Empleados")
    empleados = cur.fetchall()

    cur.close()
    return render_template('index_asignaciones.html', asignaciones=asignaciones, proyectos=proyectos, empleados=empleados)

@app.route('/empleados')
def index_empleados():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM Empleados")
    if result_value > 0:
        empleados = cur.fetchall()
        return render_template('index_empleados.html', empleados=empleados)
    return render_template('index_empleados.html')

@app.route('/add_proyecto', methods=['GET', 'POST'])
def add_proyecto():
    if request.method == 'POST':
        project_details = request.form
        nombre = project_details['nombre']
        descripcion = project_details['descripcion']
        fecha_inicio = project_details['fecha_inicio']
        fecha_fin = project_details['fecha_fin']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Proyectos (nombre, descripcion, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s)", (nombre, descripcion, fecha_inicio, fecha_fin))
        mysql.connection.commit()
        cur.close()
        flash('Proyecto agregado satisfactoriamente')
        return redirect(url_for('index_proyectos'))
    return render_template('add_proyecto.html')

@app.route('/add_empleado', methods=['GET', 'POST'])
def add_empleado():
    if request.method == 'POST':
        employee_details = request.form
        nombre = employee_details['nombre']
        email = employee_details['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Empleados (nombre, email) VALUES (%s, %s)", (nombre, email))
        mysql.connection.commit()
        cur.close()
        flash('Empleado agregado satisfactoriamente')
        return redirect(url_for('index_empleados'))
    return render_template('add_empleado.html')

@app.route('/edit_proyecto/<int:id>', methods=['GET', 'POST'])
def edit_proyecto(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Proyectos WHERE id = %s", [id])
    proyecto = cur.fetchone()
    if request.method == 'POST':
        project_details = request.form
        nombre = project_details['nombre']
        descripcion = project_details['descripcion']
        fecha_inicio = project_details['fecha_inicio']
        fecha_fin = project_details['fecha_fin']

        cur.execute("UPDATE Proyectos SET nombre = %s, descripcion = %s, fecha_inicio = %s, fecha_fin = %s WHERE id = %s", (nombre, descripcion, fecha_inicio, fecha_fin, id))
        mysql.connection.commit()
        cur.close()
        flash('Proyecto actualizado satisfactoriamente')
        return redirect(url_for('index_proyectos'))
    return render_template('edit_proyecto.html', proyecto=proyecto)

@app.route('/edit_empleado/<int:id>', methods=['GET', 'POST'])
def edit_empleado(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Empleados WHERE id = %s", [id])
    empleado = cur.fetchone()
    if request.method == 'POST':
        employee_details = request.form
        nombre = employee_details['nombre']
        email = employee_details['email']

        cur.execute("UPDATE Empleados SET nombre = %s, email = %s WHERE id = %s", (nombre, email, id))
        mysql.connection.commit()
        cur.close()
        flash('Empleado actualizado satisfactoriamente')
        return redirect(url_for('index_empleados'))
    return render_template('edit_empleado.html', empleado=empleado)

@app.route('/delete_proyecto/<int:id>', methods=['POST'])
def delete_proyecto(id):
    cur = mysql.connection.cursor()
    
    # Eliminar las asignaciones relacionadas
    cur.execute("DELETE FROM Asignaciones WHERE proyecto_id = %s", [id])
    mysql.connection.commit()

    # Eliminar el proyecto
    cur.execute("DELETE FROM Proyectos WHERE id = %s", [id])
    mysql.connection.commit()
    
    cur.close()
    flash('Proyecto eliminado satisfactoriamente')
    return redirect(url_for('index_proyectos'))

@app.route('/delete_empleado/<int:id>', methods=['POST'])
def delete_empleado(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Empleados WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Empleado eliminado satisfactoriamente')
    return redirect(url_for('index_empleados'))

@app.route('/add_asignacion', methods=['GET', 'POST'])
def add_asignacion():
    if request.method == 'POST':
        asignacion_details = request.form
        proyecto_id = asignacion_details['proyecto_id']
        empleado_id = asignacion_details['empleado_id']
        fecha_asignacion = asignacion_details['fecha_asignacion']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Asignaciones (proyecto_id, empleado_id, fecha_asignacion) VALUES (%s, %s, %s)", (proyecto_id, empleado_id, fecha_asignacion))
        mysql.connection.commit()
        cur.close()
        flash('Asignación agregada satisfactoriamente')
        return redirect(url_for('index_asignaciones'))
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nombre FROM Proyectos")
    proyectos = cur.fetchall()
    
    cur.execute("SELECT id, nombre FROM Empleados")
    empleados = cur.fetchall()
    
    cur.close()
    return render_template('add_asignacion.html', proyectos=proyectos, empleados=empleados)

@app.route('/edit_asignacion/<int:id>', methods=['GET', 'POST'])
def edit_asignacion(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Asignaciones WHERE id = %s", [id])
    asignacion = cur.fetchone()

    cur.execute("SELECT id, nombre FROM Proyectos")
    proyectos = cur.fetchall()

    cur.execute("SELECT id, nombre FROM Empleados")
    empleados = cur.fetchall()

    if request.method == 'POST':
        asignacion_details = request.form
        proyecto_id = asignacion_details['proyecto_id']
        empleado_id = asignacion_details['empleado_id']
        fecha_asignacion = asignacion_details['fecha_asignacion']

        cur.execute("UPDATE Asignaciones SET proyecto_id = %s, empleado_id = %s, fecha_asignacion = %s WHERE id = %s", (proyecto_id, empleado_id, fecha_asignacion, id))
        mysql.connection.commit()
        cur.close()
        flash('Asignación actualizada satisfactoriamente')
        return redirect(url_for('index_asignaciones'))
    return render_template('edit_asignacion.html', asignacion=asignacion, proyectos=proyectos, empleados=empleados)

@app.route('/delete_asignacion/<int:id>', methods=['POST'])
def delete_asignacion(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Asignaciones WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Asignación eliminada satisfactoriamente')
    return redirect(url_for('index_asignaciones'))

if __name__ == '__main__':
    app.run(debug=True)