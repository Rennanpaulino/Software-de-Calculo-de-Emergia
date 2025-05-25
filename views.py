from main import app

from flask import render_template

#rotas
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin")
def sign_in():
    return render_template("login.html")

@app.route("/signup")
def sign_up():
    return render_template("signup.html")

@app.route("/results")
def results():
    return render_template("results.html")    