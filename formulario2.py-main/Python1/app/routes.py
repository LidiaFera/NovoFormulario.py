from app import app, db
from flask import redirect, render_template, url_for, request #renderizar arquivo html
from flask_login import login_user, logout_user, current_user

from app.forms import ContatoForm, UserForm, LoginForm
from app.models import Contato

@app.route("/", methods = ["GET","POST"])
def homepage():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)
    return render_template("index.html", form = form)

@app.route("/codastro/", methods=['GET', 'POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for("homepage"))
    return render_template("cadastro.html", form = form)
@app.route("/sair/")
def logout():
    logout_user()
    return redirect(url_for("homepage"))



@app.route("/contato/", methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for("homepage"))
    
    return render_template("contato.html", form = form)

