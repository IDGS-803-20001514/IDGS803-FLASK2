from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField
from wtforms import validators

def mi_validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 15, message = 'No cumple la logitud del campo')
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message = 'El campo es requerido')
    ])
    apaterno = StringField('Apaterno', [mi_validacion])
    email = EmailField('Correo')

class LoginForm(Form):
    username = StringField('usuario', [
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 15, message = 'No cumple la logitud del campo')
    ])
    password = StringField('password', [
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 15, message = 'No cumple la logitud del campo')
    ])

class TradForm(Form):
    inputEspanol = StringField('Español')
    inputIngles = StringField('Inglés')
    lenguaje = RadioField('Selecciona el idioma a traducir:', choices = [('es', 'Español'), ('en', 'Inglés')])
    text = StringField('Texto')

class ResistenciaForm(Form):
    bandaUno = SelectField('Banda N1', choices = [
        ('black', 'Negro'), 
        ('maroon', 'Marrón'), 
        ('red', 'Rojo'), 
        ('orange', 'Naranja'),
        ('yellow', 'Amarillo'),
        ('green', 'Verde'),
        ('blue', 'Azul'),
        ('violet', 'Violeta'),
        ('gray', 'Gris'),
        ('white', 'Blanco')
    ])
    bandaDos = SelectField('Banda N2', choices = [
        ('black', 'Negro'), 
        ('maroon', 'Marrón'), 
        ('red', 'Rojo'), 
        ('orange', 'Naranja'),
        ('yellow', 'Amarillo'),
        ('green', 'Verde'),
        ('blue', 'Azul'),
        ('violet', 'Violeta'),
        ('gray', 'Gris'),
        ('white', 'Blanco')
    ])
    bandaTres = SelectField('Banda N3', choices = [
        ('black', 'Negro'), 
        ('maroon', 'Marrón'), 
        ('red', 'Rojo'), 
        ('orange', 'Naranja'),
        ('yellow', 'Amarillo'),
        ('green', 'Verde'),
        ('blue', 'Azul'),
        ('violet', 'Violeta'),
        ('gray', 'Gris'),
        ('white', 'Blanco')
    ])
    tolerancia = RadioField('Elige la tolerancia', [validators.DataRequired(message = 'El campo es obligatorio')], 
        choices = [
        ('gold','Oro = 5%'),
        ('silver','Plata = 10%')
    ])
