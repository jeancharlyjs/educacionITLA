# Cargar librerias
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def bienvenida():
    return render_template("index.html")

#Llamado -> debe existir
@app.route('/registro/')
def registroEstudiante():
    return render_template("registro.html")

#Captura de informacion por Request
@app.route('/registro', methods=['POST'])
def estudiantesCaputraRegistro():
    valor = request.form
    print(valor['nombre'])
    with open("registroEstudiantes.csv", 'a', encoding='UTF-8') as f:
        f.writelines("%s|%s|%s\n"%(valor['nombre'], valor['apellido'], valor['edad']))
        f.close()
    return "Excelente"

if __name__ == '__main__':
    import os
    if not os.path.exists("registroEstudiantes.csv"):
        with open("registroEstudiantes.csv", 'a', encoding='UTF-8') as f:
            f.writelines("Nombre |Apellidos |Edad\n")
            f.close()
    app.run(port=5000, debug=True)