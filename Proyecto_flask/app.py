from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola mundo con Flask";

@app.route("/productos")
def productos():
    return "Lista de productos";

app.run(debug=True)
