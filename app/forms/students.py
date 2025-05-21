from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    identification = StringField('Identificación', validators=[DataRequired()])
    firtnames = StringField('Nombres', validators=[DataRequired()])
    lastnames = StringField('Apellidos', validators=[DataRequired()])
    sex = IntegerField('Sexo', validators=[DataRequired()])
    birthdate = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Guardar')