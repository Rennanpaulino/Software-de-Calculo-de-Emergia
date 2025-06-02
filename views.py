from main import app, db
from flask import render_template, request, redirect, url_for, flash, session, send_file
from models import Produto, User
from calculator import Calculator
import pandas as pd

#rotas
@app.route("/home", methods=['GET', 'POST'])
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
        db.session.add(novo_usuario)
        db.session.commit()
        flash("Usuário criado")
        return redirect (url_for("sign_in"))

    return render_template("signup.html")

@app.route("/", methods=["GET", "POST"])
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

    df = pd.DataFrame(resultados)
    df["indice_emergético"] = indices
    df["total_emergia"]=total

    df.to_excel("static/resultados.xlsx", index=False)
    df.to_json("static/resultados.json", orient="records", indent=4)

    return render_template("results.html", resultados=resultados, total=total, indices=indices)   

@app.route("/download-excel")
def download_xlsx():
    return send_file("static/resultados.xlsx", as_attachment=True)

@app.route("/download-json")
def download_json():
    return send_file("static/resultados.json", as_attachment=True)