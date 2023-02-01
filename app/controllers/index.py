from app import app
from flask import redirect, url_for


#primeira forma de criar rotas
@app.route('/')
def index():
    return "Hello World"

# segunda forma
def test():
    return "Hola mundo "
app.add_url_rule("/teste" , "test", test)


@app.route('/home/')
@app.route('/home/<string:nome>')
def home(nome=None):
    if nome:
        return f"Seja bem vindo {nome}!"
    else:
        return f'Login não realizado'


@app.route("/admin")
def admin():
    return f"<h1>Você é administrador!</h1>"


@app.route("/login/")
@app.route("/login/<name>")
def login(name=None):
    if name == "admin":
        return redirect(url_for("admin"))
    elif name == None:
        return redirect(url_for('home'))
    else:
        return redirect(url_for("home", nome=name))







