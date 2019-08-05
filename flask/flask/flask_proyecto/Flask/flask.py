from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL 

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'conexion'
mysql= MySQL(app)


@app.route('/')
def Index():
return render_template(index.html)

@app.route('/inicio')
def Inicio():
    return render_template(login.html)

@app.route('/login')
def login():
    if request.method == 'POST':
        identificador = request.form['identificador']
        usuario = request.form['usuario']
        password = request.form['password']


@app.route('/registrar_worker', methods = ['POST'])
def registrar_worker():
    if request.method == 'POST':
    nombre_t = request.form['nombre_t']
    apellido_t = request.form['apellido_t']
    cedula_t = request.form['cedula_t']
    genero=request.form['genero']
    fecha=request.form['fecha']
    age=request.form['age']
    email=request.form['email']
    ciudad=request.form['ciudades']
    direccion=request.form['direc_t']
    telefono=request.form['tel']
    descripcion=request.form['descripcion']
    viaje=request.form['viaje']
    descripcionviaje=request.form['desc_viaje']
    calificacion=request.form['calificacion']
    quejas=request.form['quejas']
    ganancias=request.form['ganancias']
    nivel=request.form['nivel']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO trabajador (nombre_trabajador, apellido_trabajador, cedula_trabajador, genero, fecha_nacimiento, edad_trabajador, email_trabajador, id_ciudad, direc_trabajador, tel_trabajador,  descripcion, disp_viaje, desc_viaje, calificacion, nro_quejas, ganancias, codigo_nivel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', 
    (nombre_t),(apellido_t),(cedula_t),(genero_t),(fecha),(age),(email),(ciudades),(direc_t),(tel),(descripcion),(viaje),(desc_viaje),(calificacion),(quejas),(ganancias),(nivel))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/registrar_usuario)
def registrar_usuario():
return 'Bienvenido, por favor, registrate'

@app.route('/enviar_solicitud')
def enviar_solicitud():
return 'Enviar solicitud'

@app.route('/crear_contrato')
def crear_contrato():
return 'Crear contrato'

@app.route('/categoria')
if __name__ =='__main__':
app.run(port = 3000, debug = True)

