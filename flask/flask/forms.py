from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from datetime import date

# https://wtforms.readthedocs.io/en/stable/fields.html#wtforms.fields.SelectField
# https://teamtreehouse.com/community/using-wtforms-for-selectfield-in-flask
#prueba para github
class RegistrationForm(FlaskForm):
    usuario=StringField('Usuario', validators=[DataRequired(), Length(min=2, max=20)])
    identificador=StringField('Identificador', validators=[DataRequired(), Length(min=5, max=15)])
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=3, max=15), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password=PasswordField('Confirm password', validators=[DataRequired()])
    rol=SelectField('Rol', choices=[('trabajador', 'Trabajador'),('cliente', 'Cliente')])
    submit=SubmitField('Registrate aquí')

    #def validate_usuario(self, usuario):
        #usuario = usuario.query.filter_by(usuario=usuario.data).first()
        #if usuario:
         #   raise ValidationError('Este usuario ya existe.')

class LoginForm(FlaskForm):
    usuario=StringField('Usuario', validators=[DataRequired(), Length(min=2, max=20)])
    password=PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Recuerdame')
    submit=SubmitField('Ingresar')

class UsuarioForm(FlaskForm):
    cedula=StringField('Cedula', validators=[DataRequired(), Length(min=5, max=15)])
    nombre=StringField('Nombre', validators=[DataRequired(), Length(min=2, max=20)])
    apellido=StringField('Apellido', validators=[DataRequired(), Length(min=2, max=30)])
    genero=RadioField('Genero', choices=[('fem','Femenino'),('masc','Masculino')])
    fechanac=DateField('Fecha', validators=[DataRequired()], default=date.today(), format="'%d/%m/%Y'")
    #ciudad=
    email=StringField('Email', validators=[DataRequired(), Email()])
    telefono=StringField('Telefono', validators=[DataRequired(), Length(min=5, max=15)])
    direccion=StringField('Direccion', validators=[DataRequired(), Length(min=5, max=50)])
    submit=SubmitField('Crear perfil')
    

