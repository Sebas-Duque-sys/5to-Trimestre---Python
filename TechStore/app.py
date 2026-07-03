from flask import Flask, render_template, request, redirect, url_for, flash
from database.conexion import obtener_conexion

app = Flask(__name__)
app.secret_key = "adso2026"

@app.route("/")
def inicio():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("index1.html",productos=productos)

@app.route("/productos")
def productos():
    #Llamar conexión
    conexion = obtener_conexion()
    #Crear mensajero que enviara y recibira las consultas - Hace que el resultado de la consulta se guarde en un diccionario, no una lista.
    cursor = conexion.cursor(dictionary=True)
    #Grabar consulta en el mensajero
    cursor.execute("SELECT * FROM productos")
    #Guardar todos los resultados de la consulta en una variable/lista/diccionario
    productos = cursor.fetchall()
    longitud = len(productos)
    #Cerrar cursor y conexión
    cursor.close()
    conexion.close()
    return render_template("productos.html",productos=productos,longitud=longitud)

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/registro_producto")
def registro_producto():
    return render_template("registro_producto.html")

@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    precio = float(request.form["precio"])
    categoria = request.form["categoria"]

    if precio < 0:
        flash("El precio no puede ser negativo.", "error")

        return render_template(
            "registro_producto.html",
            codigo=codigo,
            nombre=nombre,
            precio=precio,
            categoria=categoria
        )
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    #Validación de existencia de código
    cursor.execute("SELECT 1 FROM productos WHERE codigo = %s", (codigo,))
    validacion = cursor.fetchone()
    #Si ya está registrado, cerrar conexión y dar mensaje de alerta
    if validacion:
        cursor.close()
        conexion.close()
        flash("El código ingresado ya existe. Por favor ingrese uno diferente.","error")
        #Devolver a formulario de registro y guardar datos ingresados.
        return render_template("registro_producto.html",codigo=codigo,nombre=nombre,precio=precio,categoria=categoria)
    
    #Si no está registrado, realizar registro
    sql = """ INSERT INTO productos VALUES (%s,%s,%s,%s) """
    cursor.execute(sql,(codigo,nombre,precio,categoria))
    #Guardan los cambios realizados por la consulta
    conexion.commit()
    #Mensaje de exito:
    flash ("Producto registrado exitosamente", "success")
    cursor.close()
    conexion.close()

    #Regreso a la tabla
    return redirect(url_for("productos"))

@app.route("/editar_producto/<codigo>")
def editar_producto(codigo):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    sql = """ SELECT * FROM productos WHERE codigo = %s ;"""
    cursor.execute(sql,(codigo,))
    producto = cursor.fetchone()
    cursor.close()
    conexion.close()
    return render_template("editar_producto.html",producto=producto)

@app.route("/actualizar_producto",methods=["POST"])
def actualizar_producto():
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """ UPDATE productos SET nombre = %s, precio = %s, categoria = %s WHERE codigo = %s """
    cursor.execute(
        sql,
        (
            nombre,
            precio,
            categoria,
            codigo
        )
    )
    conexion.commit() 
    flash ("Producto actualizado exitosamente", "success")
    cursor.close()
    conexion.close()
    return redirect(url_for("productos"))

@app.route("/eliminar_producto/<codigo>")
def eliminar_producto(codigo):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    sql = "DELETE FROM productos WHERE codigo = %s"
    cursor.execute(sql,(codigo,))
    conexion.commit()
    producto = cursor.fetchone()
    flash ("Producto eliminado correctamente", "success")
    cursor.close()
    conexion.close
    return redirect(url_for("productos"))

app.run(debug=True)