from flask import Flask, render_template, request, redirect ,url_for, session
from bd_login import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'teste'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/perfil")
def perfil():
	try:
		if session["usuario"]:
			usuario = Usuario.select().where(Usuario.nome == session["usuario"])
		else:
			usuario = False
	except:
		session["usuario"] = False
		return redirect("/perfil")
	return render_template("perfil.html", usuario = usuario)

@app.route("/form_editar_informacoes")
def form_editar_informacoes():
	usuario = Usuario.select().where(Usuario.nome == session["usuario"])
	return render_template("form_editar_informacoes.html", usuario = usuario)

@app.route("/editar_informacoes")
def editar_informacoes():
	usuario = Usuario.select().where(Usuario.nome == session["usuario"])
	nome = request.args.get("nome")
	email = request.args.get("email")
	telefone = request.args.get("tel")
	nascimento = request.args.get("nascimento")
	endereco = request.args.get("end")
	senha = request.args.get("senha")
	confsenha = request.args.get("confsenha")
	vaziu = request.args.get("vaziu")
	
	session["usuario"] = nome
	if len(senha) > 8 and  senha == confsenha and senha != vaziu:
		Usuario.update(nome = nome, email = email, telefone = telefone, nascimento = nascimento, endereco = endereco, senha = senha).execute()
	elif senha == vaziu:
		Usuario.update(nome = nome, email = email, telefone = telefone, nascimento = nascimento, endereco = endereco).execute()
	else: 
		return render_template("senha_incorreta.html", destino = "/form_editar_informacoes")
	return redirect("/perfil")


@app.route("/logout")
def logout():
	session["usuario"] = False
	return redirect("/form_login")

@app.route("/tutoriais")
def tutoriais():
	return render_template("tutoriais.html")

@app.route("/tutorial1")
def tutorial1():
	return render_template("tutorial1.html")

@app.route("/tutorial2")
def tutorial2():
	return render_template("tutorial2.html")

@app.route("/tutorial3")
def tutorial3():
	return render_template("tutorial3.html")
	
@app.route("/tutorial4")
def tutorial4():
	return render_template("tutorial4.html")

@app.route("/tutorial5")
def tutorial5():
	return render_template("tutorial5.html")

@app.route("/tutorial6")
def tutorial6():
	return render_template("tutorial6.html")

@app.route("/tutorial7")
def tutorial7():
	return render_template("tutorial7.html")

@app.route("/tutorial8")
def tutorial8():
	return render_template("tutorial8.html")

@app.route("/tutorial9")
def tutorial9():
	return render_template("tutorial9.html")

@app.route("/contato")
def contato():
	return render_template("contato.html")


@app.route("/enviar_duvida")
def enviar_duvida():
	nome = request.args.get("nome")
	email = request.args.get("email")
	tel = request.args.get("tel")
	duvida = request.args.get("duvida")
	Duvida(nome = nome, email = email, telefone = tel, duvida = duvida).save()
	return render_template("duvida_enviada.html")

@app.route("/aboutus")
def aboutus():
	return render_template("aboutus.html")

@app.route("/form_login")
def form_login():
	return render_template("form_login.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
	login = request.args.get("nome")
	senha = request.args.get("senha")
	usuario = Usuario.select().where(Usuario.nome == login)
	for u in usuario:
		print("usuario")
		if login == u.nome and senha == u.senha: 
			session['usuario'] = login
			print("login")
			return redirect("/perfil")
	return redirect("/form_login")

@app.route("/form_cadastro")
def form_cadastro():
	return render_template("form_cadastro.html")

@app.route("/cadastrar", methods = ['GET', 'POST'])
def cadastrar():
	nome = request.args.get("nome")
	email = request.args.get("email")
	telefone = request.args.get("tel")
	nascimento = request.args.get("nascimento")
	endereco = request.args.get("end")
	senha = request.args.get("senha")
	confsenha = request.args.get("confsenha")
	vaziu = request.args.get("vaziu")
	if len(senha) > 8 and  senha == confsenha and senha != vaziu:
		Usuario.create(nome = nome, email = email, telefone = telefone, nascimento = nascimento, endereco = endereco, senha = senha)
	else:
		return render_template("senha_incorreta.html", destino = "/form_cadastro")
	return redirect("/form_login")

#@app.route("/submit_duvidas")
#def submit_duvidas


app.run(debug=True)