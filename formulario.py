from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

class FormInicio (FlaskForm):
    # la variable nombre de tipo StringField equivale a un input de tipo text
    nombre = StringField ('Nombre Usuario: ', validators=[DataRequired(message='Nombre es Obligatorio'),
    Length(min=5, max=10,message="Usuario debe tener entre 5 y 10 caracteres")])

    passWd= PasswordField ('Contraseña: ', validators=[DataRequired('La contraseña en necesaria')])

    recordar = BooleanField('Recordar Usuario')

    enviar = SubmitField('Iniciar Sesión')
