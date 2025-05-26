from main import app
from flask import render_template, request
from models import Produto, Insumos
from calculator import *

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

@app.route("/signin")
def sign_in():
    return render_template("login.html")

@app.route("/signup")
def sign_up():
    return render_template("signup.html")

@app.route("/results", methods=["POST"])
def results():
    calc = Calculator()
    resu, total = calc.calculator(request.form)
    return render_template("results.html", resultados =resu, total=total)    

# @app.route("/teste")
# def teste():
#     garrafa = Produto.query.filter_by(item="Garrafa de Vidro").first()
#     if garrafa:
#         for i in garrafa.insumos:
#             print(i.insumo, i.unidade, i.UEV)
#         return "Insumos impressos no console."
#     else:
#         print("Produto não encontrado.")
#         return "Produto não encontrado."