from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bienvenido al sistema";

@app.route("/saludo")
def saludo():
    return "Hola aprendiz ADSO";

@app.route("/inventario")
def inventario():
    return "Sistema inventario activo";

@app.route("/usuarios")
def usuarios():
    return "Sistema usuarios activo";

app.run(debug=True)