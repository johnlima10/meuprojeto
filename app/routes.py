from app import app
from flask import render_template

@app.route('/')
#@app.route('/index')

def index():
    #return "Olá mundo"
    return render_template('index.html',titulo = 'Página inicial')

@app.route('/contatos')
def contatos():
    #return "Projetos"
    return render_template('contatos.html',titulo = 'Contatos')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html',titulo = 'Sobre')