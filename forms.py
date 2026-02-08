from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, RadioField
from wtforms.validators import DataRequired, NumberRange, Email

class UserForm(FlaskForm):
    matricula = IntegerField(
        "Matricula",
        validators=[DataRequired(message="La matrícula es obligatoria")]
    )
    nombre = StringField(
        "Nombre",
        validators=[DataRequired(message="El nombre es obligatorio")]
    )
    apellido = StringField(
        "Apellido",
        validators=[DataRequired(message="El apellido es obligatorio")]
    )
    correo = EmailField(
        "Email",
        validators=[
            DataRequired(message="El correo es obligatorio"),
            Email(message="Ingresa un correo válido")
        ]
    )


class CinepolisForm(FlaskForm):
    nombre = StringField(
        "Nombre del cliente",
        validators=[DataRequired(message="El nombre es obligatorio")]
    )

    compradores = IntegerField(
    "Número de Compradores",
    validators=[
        DataRequired(message="La cantidad de compradores es obligatoria"),
        NumberRange(min=1, message="La cantidad minima de compradores es 1")
    ],
    filters=[lambda x: x or None]  # <-- esto evita errores de conversión vacíos
)


    boletos = IntegerField(
        "Número de boletos",
        validators=[
            DataRequired(message="La cantidad de boletos es obligatoria"),
            NumberRange(min=1, max=7, message="Solo se pueden comprar de 1 a 7 boletos")
        ]
    )

    cineco = RadioField(
        "Tarjeta Cineco",
        choices=[('si', 'Sí'), ('no', 'No')],
        validators=[DataRequired(message="Debes seleccionar una opción")]
    )