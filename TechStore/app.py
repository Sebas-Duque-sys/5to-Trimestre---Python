from flask import Flask, render_template, request
from database.conexion import obtener_conexion

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index1.html")

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
    #Cerrar cursor y conexión
    cursor.close()
    conexion.close()
    return render_template("productos.html",productos=productos)

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
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    return render_template(
        "respuesta.html",
        codigo=codigo,
        nombre=nombre,
        precio=precio,
        categoria=categoria
    )

app.run(debug=True)