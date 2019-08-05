from flask import Flask, render_template, request, redirect, url_for, flash, json
from flask_mysqldb import MySQL
from forms import RegistrationForm, LoginForm, UsuarioForm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,  SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '184f79a3875670a1c604b03a5c7b3a89'


#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'conexion'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
bcrypt = Bcrypt(app)
mysql= MySQL(app)

#Sesion-conexion 
app.secret_key = 'mysecretkey'

posts = [
        {
                'trabajador': 'Milena',
                'categoria': 'Conductor Bilingue',
                'descripcion': 'Licenciada en idiomas de la UIS',
                'calificacion': '4.87',
         },
         {
                 'trabajador': 'Laura',
                 'categoria': 'Daycare',
                 'descripcion': 'Amo los animales',
                 'calificacion': '4.65',
         }
]

#Home Page
@app.route('/')
def Index():
    return render_template('index.html')

#SignUp
@app.route('/signup', methods=['GET','POST'])
def signup():
        #https://www.youtube.com/watch?v=6L3HNyXEais&t=728s -> Formulario (Indu)
        form = RegistrationForm()
        if request.method == 'POST':
                if form.validate_on_submit():
                        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                        identificador = request.form['identificador']
                        usuario = request.form['usuario']
                        password = request.form['password']
                        email = request.form['email']
                        rol = request.form['rol']
                        print(identificador)
                        print(usuario)
                        #print(password)
                        cur = mysql.connection.cursor()
                        cur.execute('INSERT INTO login (identificador, usuario, password, email, rol) VALUES (%s,%s,%s,%s,%s)', (identificador, usuario, hashed_password, email, rol))
                        mysql.connection.commit()
                        cur.close()
                        flash(f'Cuenta creada para {form.usuario.data}! Ya puedes iniciar sesion', 'success')
                        return redirect(url_for('login'))
        return render_template('signup.html', form=form)
        
#@app.route('/register', methods = ['POST'])
#def register():
        #if request.method == 'POST':
        #        identificador = request.form['identificador']
        #        usuario = request.form['usuario']
         #       password = request.form['password']
          #      rol = request.form['rol']
           #     print(identificador)
            #    print(usuario)
             #   print(password)
              #  cur = mysql.connection.cursor()
               # cur.execute('INSERT INTO login2 (identificador, usuario, password, rol) VALUES (%s,%s,%s,%s)', (identificador, usuario, password, rol))
                #mysql.connection.commit()
                #cur.close()
                #return redirect(url_for('perfil'))
        # redireccionar a formulario de registro 
        # un return --> return redirect(url_for('registrarsetr'))

#Login
@app.route('/iniciosesion', methods=['GET', 'POST'])
def iniciosesion():
        form = LoginForm()
        if form.validate_on_submit():
                if form.usuario.data == 'danielannah' and form.password.data == 'password':
                       flash('Felicitaciones', 'success')
                       return redirect(url_for('perfil'))
                else:
                        flash('Paila menor', 'danger')
        return render_template('login.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
        #if request.method == 'POST'
        #usuario = request.form['usuario']
        #password = request.form['password']
        #cur=mysql.connection.cursor()
        #result = cur.execute("SELECT * FROM login2 WHERE usuario = %s, [usuario]")

        #if result > 0:
        #        data = cursor.fetchone()
        #        password = data['password']

                
        form = LoginForm()
        if form.validate_on_submit():
                if form.usuario.data == 'danielannah' and form.password.data == 'password':
                        flash('Felicitaciones', 'success')
                        return redirect(url_for('Index'))
                else:
                        flash('Paila menor', 'danger')
        return render_template('login.html', form=form)

#Crear Perfil
@app.route('/perfil')
def perfil():
        return render_template('perfil.html')

#Trabajador
@app.route('/registrarsetr')
def registrarse():
        #cur= mysql.connection.cursor()
        #cur.execute('SELECT * FROM trabajador')
        #data = cur.fetchall()
        #print(data)
        return render_template('reg_trabajador.html')
        # tabla con los datos ->
        #return render_template('reg_trabajador.html', trabajadores= data)

#Formulario trabajador
@app.route('/registrar_trabajador', methods = ['POST'])
def registrar_trabajador():
    if request.method=='POST':
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
        #cur = mysql.connection.cursor()
        #cur.execute('INSERT INTO trabajador (nombre_trabajador, apellido_trabajador, cedula_trabajador, genero, fecha_nacimiento, edad_trabajador, email_trabajador, id_ciudad, direc_trabajador, tel_trabajador,  descripcion, disp_viaje, desc_viaje, calificacion, nro_quejas, ganancias, codigo_nivel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', 
        #(nombre_t),(apellido_t),(cedula_t),(genero_t),(fecha),(age),(email),(ciudades),(direc_t),(tel),(descripcion),(viaje),(desc_viaje),(calificacion),(quejas),(ganancias),(nivel))
        #mysql.connection.commit()
        flash('Perfil creado')
        return redirect(url_for('perfiltra'))

@app.route('/perfiltra')
def perfiltra():
        return render_template('perfil_tra.html',  posts=posts, nombre='Laura')

#Usuario
@app.route('/registrarseus')
def registrar_us():
        form = UsuarioForm()
        if form.validate_on_submit():
                flash(f'Perfil creado', 'success')
                return redirect(url_for('perfilus'))
        return render_template('reg_usuario.html', form=form)
        #cur= mysql.connection.cursor()
        #cur.execute('SELECT * FROM usuario')
        #data = cur.fetchall()
        #print(data)
        #return render_template('reg_usuario.html, usuarios = data)
        #Hace falta crear la ruta eliminar y ruta update para usuario

@app.route('/registrar_usuario', methods = ['POST'])
def registrar_usuario():
        if request.method == 'POST':
                nombre=request.form['nombre']
                apellido=request.form['apellido']
                cedula=request.form['cedula']
                genero=request.form['genero']
                fecha=request.form['fechanac']
                email=request.form['email']
                #ciudades=request.form['ciudad']
                direccion=request.form['direccion']
                telefono=request.form['telefono']
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO usuario2 (nombre_usuario, apellido_usuario, cedula_usuario, fecha_nacimiento, correo_usuario, direc_usuario, tel_usuario) VALUES (%s, %s, %s, %s, %s, %s, %s)",(nombre,apellido,cedula,fecha,email,direccion,telefono))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('perfilus'))


@app.route('/perfilus')
def perfilus():
        return render_template('perfil_us.html',  posts=posts)

#Categoria
@app.route('/categoria')
def categoria():
        return render_template('categoria.html')

#Contrato
@app.route('/contrato')
def contrato():
        return render_template('contrato.html')

@app.route('/crearcontrato', methods = ['POST'])
def crearcontrato():
        if request.method=='POST':
                contrato=request.form['contrato']
                solicitud=request.form['solicitud']
                fechain=request.form['fechain']
                fechafi=request.form['fechafi']
                direc=request.form['direc']
                duracion=request.form['duracion']
                valor=request.form['valor']
                materiales=request.form['materiales']
                transporte=request.form['transporte']
                total=request.form['total']
                #cur = mysql.connection.cursor()
                #cur.execute('INSERT INTO contrato (numero_contrato, valor_servicio, nro_horas, direccion_contrato, fecha_inicio, fecha_finalizacion, cod_solicitud, costo_materiales, transporte, total) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',
                #(contrato),(valor), (duracion), (direc), (fechain), (fechafi), (solicitud), (materiales), (transporte), (total))
                #mysql.connection.commit()
                flash('Contrato creado')
                return redirect(url_for('perfil'))

#Editar
@app.route('/editar')
def editar_contacto(cedula):
        cur = mysql.connection.curor()
        cur.execute('SELECT * FROM trabajador WHERE cedula = %s', (cedula))
        data = cur.fetchall()
        return render_template('edit.html', contactos = data[0])

@app.route('/update/<cedula>', methods=['POST'])
def update(cedula):
        if request.method == 'POST':
                nombre_t = request.form['nombre_t']
                email = request.form['email']
                telefono = request.form['telefono']
        #cur = mysql.connection.cursor()
        #cur.execute(""" UPDATE trabajador SET nombre_t = %s,
        #email = %s,
        #telefono = %s
        #where cedula=%s """, (nombre_t, email, telefono, cedula))
        #mysql.connection.commit()
        flash('Perfil actualizado')
        return redirect(url_for('/perfiltra'))

#Eliminar
#@app.route('/delete/<string:varchar(10)>')
#def delete(cedula):
#        return print(cedula)
#        cur = mysql.connection.cursor()
#        cur.execute('DELETE FROM trabajador WHERE cedula={0}'.format(cedula))
#        mysql.connection.commit()
#flash('Contact Removed Succesfully')
#        return redirect(url_for('Index'))


@app.route('/eliminar_cuenta')
def eliminar_cuenta():
    return 'eliminar'

if __name__ == '__main__':
    app.run(port=3000, debug = True)