from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
from database.conexion import obtener_conexion
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import io
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

@app.route("/exportar_productos")
def exportar_productos():
    #Realizar consulta
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    longitud = len(productos)
    cursor.close()
    conexion.close()
    #Lo que entendi al crear esto.
    #pdf = canvas.Canvas() ==== canvas llama a la libreria. Canvas llama al modulo para crear un documento y dicho documento queda bajo la variable 'pdf'
    #buffer es para crear un archivo temporal en el navegador en lugar de usar un archivo permanente o local
    #pagesize=letter Es el tamaño de la página. letter es tamaño carta
    #setFont = Define una fuente y un tamaño de letra para lo que se va a escribir
    #drawString = Define que se va a escribir y en que posición. El primer valor el posición horizontal y la segunda es posición vertical
    #y = Al ir definiendola y luego modificandola con calculos, creo lineas de escritura
    #as_attachment=True. Define que es un archivo descargable
    #download_name="lista_de_productos.pdf" Nombre del archivo a descargar
    #mimetype="application/pdf" Define el formato en el que se genera el archivo
    #1- Crear archivo
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    #Titulo
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(200, 750, "TechStore")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(180, 730, "Listado de productos")
    y = 690
    #Encabezado
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, y, "Código")
    pdf.drawString(130, y, "Nombre")
    pdf.drawString(300, y, "Precio")
    pdf.drawString(400, y, "Categoría")
    y -= 20
    #Contenido
    pdf.setFont("Helvetica", 9)
    for producto in productos:
        pdf.drawString(50, y, producto["codigo"])
        pdf.drawString(130, y, producto["nombre"])
        pdf.drawString(300, y, "$"+str(producto["precio"]))
        pdf.drawString(400, y, producto["categoria"])
        y -= 20
        #Crear nuevas páginas cuando se llegue al borde
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 9)
            y = 750

    #Guardar PDF
    pdf.save()
    buffer.seek(0)
    #Enviar como descargable al navegador
    return send_file(
        buffer,
        as_attachment=True,
        download_name="lista_de_productos.pdf",
        mimetype="application/pdf"
    )
    return render_template("productos.html",productos=productos,longitud=longitud)

@app.route("/signup", methods=["POST"])
def signup():
        #Recibir datos del formulario
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        telefono = request.form.get("telefono")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
    #Validaciones
        #Contraseñas iguales
        if password1 != password2:
            flash("Las contraseñas ingresadas no son iguales.", "error")
            return redirect(url_for("inicio"))
        #Conexión a la base de datos
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        #Validación de correo duplicado
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        validacion = cursor.fetchone()
        if validacion:
            flash("El correo ingresado ya está registrado. Por favor ingrese uno diferente.", "error")
            # return redirect(url_for("inicio"))
            return redirect(url_for("inicio"))
        #Registro del usuario
        sql = """INSERT INTO usuarios (nombre, correo, telefono, password) VALUES (%s,%s, %s, %s)"""
        cursor.execute(sql, (nombre, correo, telefono, password1))
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
        session["correo"] = usuario["correo"]
        rol = usuario["rol"]
        if rol == "Administrador":
            return redirect(url_for("admin"))
        else:
            return redirect(url_for("perfil"))
    else:
        flash("Correo o contraseña incorrectos", "error")
        return redirect(url_for("inicio"))
    
@app.route("/admin")
def admin():
    if "usuario" not in session:
        return redirect(url_for("inicio"))
    return render_template("admin.html")

@app.route("/perfil")
def perfil():
    if "usuario" not in session:
        return redirect(url_for("inicio"))
    #Consultar perfil
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    sql = """ SELECT * FROM usuarios WHERE correo = %s """
    correo = (session["correo"])
    cursor.execute(sql, (correo,))
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()
    return render_template("perfil.html",usuario=usuario)

@app.route("/actualizar_perfil",methods=["POST"])
def actualizar_perfil():
    if "usuario" not in session:
        return redirect(url_for("inicio"))

    nombre = request.form["nombre"]
    correo = request.form["correo"]
    telefono = request.form["telefono"]
    password0 = request.form["password0"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    #Verificar contraseña
    sql = """ SELECT * FROM usuarios WHERE correo = %s AND password = %s """
    cursor.execute(sql,(correo, password0))
    usuario = cursor.fetchone()
    if usuario:
        #Actualizar usuario
        sql = """ UPDATE usuarios SET nombre = %s, telefono = %s WHERE correo = %s """
        cursor.execute(sql,(nombre,telefono,correo))
        conexion.commit()
        flash ("Perfil actualizado exitosamente", "success")
        cursor.close()
        conexion.close()
        return redirect(url_for("perfil"))
    else:
        #Error en contraseña
        flash ("Contraseña incorrecta", "error")
        cursor.close()
        conexion.close()
        return redirect(url_for("perfil"))

@app.route("/actualizar_contraseña",methods=["POST"])
def actualizar_contraseña():
    if "usuario" not in session:
        return redirect(url_for("inicio"))

    correo = request.form["correo"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    password3 = request.form["password3"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    #Verificar igualdad en contraseñas
    if password2 != password3:
        flash("Las contraseñas ingresadas no son iguales.", "error")
        return redirect(url_for("inicio"))
    #Verificar contraseña actual
    sql = """ SELECT * FROM usuarios WHERE correo = %s AND password = %s """
    cursor.execute(sql,(correo, password1))
    usuario = cursor.fetchone()
    if usuario:
        #Verificar que la nueva contraseña no sea igual
        if password2 == password1:
            flash("La nueva contraseña no puede ser igual a la actual.", "error")
            cursor.close()
            conexion.close()
            return redirect(url_for("perfil"))
        #Actualizar contraseña
        sql = """ UPDATE usuarios SET password = %s WHERE correo = %s """
        cursor.execute(sql,(password2,correo))
        conexion.commit()
        flash ("Contraseña actualizada exitosamente", "success")
        cursor.close()
        conexion.close()
        return redirect(url_for("perfil"))
    else:
        #Error en contraseña
        flash ("Contraseña incorrecta", "error")
        cursor.close()
        conexion.close()
        return redirect(url_for("perfil"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("inicio"))

@app.route("/pruebas")
def pruebas():
    correo = 'cliente1@gmail.com'
    password = 'Prueba'
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    sql = """SELECT * FROM usuarios WHERE correo = %s AND password = %s AND estado = 'activo'"""
    cursor.execute(sql, (correo, password))
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()
    sesion = session["rol"]
    return sesion
app.run(debug=True)