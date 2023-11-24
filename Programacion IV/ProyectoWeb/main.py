from flask import Flask, render_template
import psycopg2
from flask import request
import os

app = Flask(__name__)

#CONEXION A BASE DATOS

DB_HOST = ''
DB_PORT
DB_BASE
DB_USER
DB_PASS


@app.route('/')
def bienvenida():
	return render_template('index.html')

@app.route('/registro/')
def registroEstudiantes():
	return render_template("registro.html")

@app.route('/registro', methods=['POST'])
def estudiantesRegistro():
	valor = request.form
	print(valor['nombre'])
	print(valor['apellido'])
	print(valor['edad'])
	return "<script> alert('Excelente')</script>"
if __name__ == '__main__':
	app.run(port=5000, debug=True)