from app import app
from flask import render_template

@app.route('/')
#@app.route('/index')

def index():
    #return "Olá mundo"
    return render_template('index.html',titulo = 'Página inicial')

@app.route('/projetos')
def projetos():
    #return "Projetos"
    return render_template('projetos.html',titulo = 'Projetos')