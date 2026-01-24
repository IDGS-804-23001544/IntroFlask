from flask import Flask, render_template, request
import math
from forms import UserForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'clave_secreta'

csrf = CSRFProtect(app)





@app.route('/')
def index():
    title = "IDGS804 - Intro Flask"
    listado = ['Juan', 'Ana', 'Pedro', 'Tadeo']
    return render_template('index.html')


# ---------------- OPERACIONES BÁSICAS ----------------
@app.route("/operasBase", methods=['GET', 'POST'])
def operasbas():
    res = None

    if request.method == 'POST':
        n1 = request.form.get('num1')
        n2 = request.form.get('num2')
        operacion = request.form.get('operacion')

        n1 = float(n1)
        n2 = float(n2)

        if operacion == 'sumar':
            res = n1 + n2
        elif operacion == 'restar':
            res = n1 - n2
        elif operacion == 'dividir':
            res = n1 / n2
        elif operacion == 'multiplicar':
            res = n1 * n2

    return render_template("operasBase.html", res=res)


# ---------------- DISTANCIA ENTRE DOS PUNTOS ----------------
@app.route("/distancia", methods=["GET", "POST"])
def calcular_distancia():
    resultado = None

    if request.method == "POST":
        try:
            punto1_x = float(request.form.get("x1"))
            punto1_y = float(request.form.get("y1"))
            punto2_x = float(request.form.get("x2"))
            punto2_y = float(request.form.get("y2"))

            dx = punto2_x - punto1_x
            dy = punto2_y - punto1_y

            resultado = math.hypot(dx, dy)
        except (TypeError, ValueError):
            resultado = None

    return render_template("distancia.html", distancia=resultado)


# ---------------- RUTAS DE EJEMPLO ----------------
@app.route("/resultado", methods=['GET', 'POST'])
def result1():
    n1 = float(request.form.get('num1'))
    n2 = float(request.form.get('num2'))
    return f"<h1>La suma es: {n1 + n2}</h1>"


@app.route("/hola")
def hola():
    return 'Hola, Nueva Ruta!!'


@app.route("/user/<string:user>")
def user(user):
    return f'Hola, {user}!'


@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1>Number, {n}!</h1>'


@app.route("/username/<int:id>/<string:username>")
def username(id, username):
    return f'<h1>Hola, {username}, tu id es: {id}</h1>'


@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f'<h1>La suma es: {n1 + n2}</h1>'


@app.route('/operas')
def operas():
    return '''
        <form>
        <label> Nombre: </label>
        <input type="text" required><br>
        <label> Paterno: </label>
        <input type="text" required><br>
        <label> Password: </label>
        <input type="password"><br>
        <input type="submit" value="Enviar">
        </form>
    '''
@app.route("/alumnos", methods=["GET", "POST"])
def alumno():
    mat = nom = ape = email = ""
    alumno_class = forms.UserForm()

    if alumno_class.validate_on_submit():
        mat = alumno_class.matricula.data
        nom = alumno_class.nombre.data
        ape = alumno_class.apellido.data
        email = alumno_class.correo.data

    return render_template(
        "alumnos.html",
        form=alumno_class,
        mat=mat,
        nom=nom,
        ape=ape,
        email=email
    )
# ---------------- EJECUCIÓN ----------------
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5050, debug=True)
