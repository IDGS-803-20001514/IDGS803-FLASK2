from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField

class UseForm(Form):
    matricula = StringField('Matricula')
    nombre = StringField('Nombre')
    apeterno = StringField('Apellido Paterno')
    email = EmailField('Correo')
