from flask import Flask, render_template, request, redirect, url_for, flash, session
from database.conexion import obtener_conexion
import re
#import session

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
    if "usuario" not in session:
        return redirect(url_for("inicio"))
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
    if "usuario" not in session:
        return redirect(url_for("inicio"))
    return render_template("registro_producto.html")

@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    #Validación 1: .strip() Elimina espacios en blanco al inicio y al final de la cadena.
    codigo = request.form.get("codigo", "").strip()
    nombre = request.form.get("nombre", "").strip()
    precio = request.form.get("precio", "").strip()
    categoria = request.form.get("categoria", "").strip()
    #Validación 2: Validar que los campos no estén vacíos.
    if not codigo or not nombre or not precio or not categoria:
        flash("Todos los campos son obligatorios.", "error")
        #Devolver a formulario de registro y guardar datos ingresados.
        return render_template("registro_producto.html",codigo=codigo,nombre=nombre,precio=precio,categoria=categoria)

    #Convertir precio a decimal. También se valida que el precio sea un número válido.
    try:
        precio = float(precio)
    except ValueError:
        flash("El precio ingresado no es un número válido.", "error")
        return render_template("registro_producto.html",codigo=codigo,nombre=nombre,precio=precio,categoria=categoria)
    
    #Validaciones de Precios
    #Validación 3: Validar que el precio sea mayor a cero.
    if precio <= 0:
        flash("El precio no puede ser negativo.", "error")
        #Devolver a formulario de registro y guardar datos ingresados.
        return render_template(
            "registro_producto.html",
            codigo=codigo,
            nombre=nombre,
            precio=precio,
            categoria=categoria
        )
    #Validación 8: Validar que el precio no sea mayor a 5.000.000
    elif precio > 500000:
        flash("El precio no puede ser mayor a 5.000.000", "error")
        return render_template("registro_producto.html",codigo=codigo,nombre=nombre,precio=precio,categoria=categoria)
    
    #Validaciones de Caracteres
    #Validación 5: Validar que el código tenga al menos 5 caracteres.    
    if len(codigo) < 4:
        flash("El código del producto debe tener al menos 4 caracteres.", "error")
        return render_template("registro_producto.html",codigo=codigo,nombre=nombre,precio=precio,categoria=categoria)
    #Validación 8: Validar que el código no tenga más de 100 caracteres.
    elif len(codigo) > 100:
        flash("El código del producto no puede tener más de 100 caracteres.", "error")
        return render_template("registro_producto.html",codigo=codigo,nombre=nombre,precio=precio,categoria=categoria)
    #Validación 6: Validar que el nombre tenga al menos 5 caracteres.
    if len(nombre) <= 5:
            flash("El nombre del producto debe tener al menos 5 caracteres.", "error")
            return render_template("registro_producto.html",codigo=codigo,nombre=nombre,precio=precio,categoria=categoria)
    #Validación 8: Validar que el nombre no tenga más de 100 caracteres.
    elif len(nombre) > 100:
            flash("El nombre del producto no puede tener más de 100 caracteres.", "error")
            return render_template("registro_producto.html",codigo=codigo,nombre=nombre,precio=precio,categoria=categoria)

    #Validación 7: Validar que siga el patron de P001, P002
    patron = r"^P00\d+$"
    if not re.match(patron, codigo):
        flash("El código del producto no sigue el patrón requerido (POO1, POO2, etc.).", "error")
        return render_template("registro_producto.html",codigo=codigo,nombre=nombre,precio=precio,categoria=categoria)

    #Conexión a la base de datos
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    #Validación 4: Código duplicado
    cursor.execute("SELECT 1 FROM productos WHERE codigo = %s", (codigo,))
    validacion = cursor.fetchone()
    #Si ya está registrado, cerrar conexión y dar mensaje de alerta
    if validacion:
        cursor.close()
        conexion.close()
        flash("El código ingresado ya existe. Por favor ingrese uno diferente.","error")
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
    if "usuario" not in session:
       return redirect(url_for("inicio"))
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
    if "usuario" not in session:
        return redirect(url_for("inicio"))

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
    if "usuario" not in session:
        return redirect(url_for("inicio"))

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    sql = "DELETE FROM productos WHERE codigo = %s"
    cursor.execute(sql,(codigo,))
    conexion.commit()
    flash ("Producto eliminado correctamente", "success")
    cursor.close()
    conexion.close()
    return redirect(url_for("productos"))

@app.route("/signup", methods=["POST"])
def signup():
        #Recibir datos del formulario
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        password = request.form.get("password")
        
        #Validaciones
        
        #Conexión a la base de datos
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        #Validación de correo duplicado
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        validacion = cursor.fetchone()
        if validacion:
            flash("El correo ingresado ya está registrado. Por favor ingrese uno diferente.", "error")
            return redirect(url_for("inicio"))
        #Registro del usuario
        sql = """INSERT INTO usuarios (nombre, correo, password) VALUES (%s, %s, %s)"""
        cursor.execute(sql, (nombre, correo, password))
        conexion.commit()
        flash("Usuario registrado exitosamente", "success") 
        cursor.close()
        conexion.close()
        return redirect(url_for("inicio"))

@app.route("/login", methods=["POST"])
def login():
    if "usuario" in session:
        return redirect(url_for("inicio"))

    correo = request.form.get("correo")
    password = request.form.get("password")
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    sql = """SELECT * FROM usuarios WHERE correo = %s AND password = %s AND estado = 'activo'"""
    cursor.execute(sql, (correo, password))
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()

    if usuario:
        session["usuario"] = usuario["nombre"]
        session["rol"] = usuario["rol"]
        return redirect(url_for("admin"))
    else:
        flash("Correo o contraseña incorrectos", "danger")
        return redirect(url_for("inicio"))
    
@app.route("/admin")
def admin():
    if "usuario" not in session:
        return redirect(url_for("inicio"))
    return render_template("admin.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("inicio"))

app.run(debug=True)