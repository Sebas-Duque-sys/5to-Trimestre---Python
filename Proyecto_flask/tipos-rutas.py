from flask import Flask

app = Flask(__name__)

@app.route("/contacto")
def inicio():
    return "Página de contacto";

#127.0.0.1:5000/usuario/juan
@app.route("/usuario/<nombre>")
def usuario(nombre):
    return f"Bienvenido: {nombre}";

app.run(debug=True)