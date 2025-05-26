from main import app, bcrypt
from flask import render_template, request, redirect, url_for, flash, session
from models import Produto, Insumos, User, db
from calculator import Calculator

#rotas
@app.route("/", methods=['GET', 'POST'])
def index():
    produto = None
    insumos = []

    if request.method=='GET':
        nome = request.args.get("produto")
        if nome:
            produto = Produto.query.filter_by(item=nome).first()
            if produto:
                insumos = produto.insumos

    return render_template("index.html", produto=produto, insumos=insumos)

@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        if User.query.filter_by(email=email).first():
            flash("Email já cadastrado!")
            return redirect(url_for("sign_up"))
        
        novo_usuario = User(nome=nome, email=email)
        novo_usuario.setSenha(senha)
        db.session.commit()
        flash("Usuário criado")
        return redirect (url_for("sign_in"))

    return render_template("signup.html")

@app.route("/signin", methods=["GET", "POST"])
def sign_in():
    if request.method=='POST':
        email=request.form["email"]
        senha = request.form["senha"]
        usuario = User.query.filter_by(email=email).first()

        if usuario and usuario.verifySenha(senha):
            session["usuario_id"] = usuario.id
            session["usuario_nome"] = usuario.nome
            flash("Login efetuado com sucesso")
            return redirect(url_for("index"))
        else: 
            flash("Email ou senha inválidos")

    return render_template("login.html")

@app.route("/results", methods=["POST"])
def results():
    calc = Calculator()
    resultados, total, indices = calc.calculator(request.form)
    return render_template("results.html", resultados=resultados, total=total, indices=indices)   
