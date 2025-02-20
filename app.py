from flask import Flask, render_template, request, redirect,g
import requests # requisição para usarmos as APIs
import sqlite3

def ligar_banco():
    banco = g.database = sqlite3.connect('API-Imagens.db')
    return banco

API_KEY = 'live_ANubS9tHsUEVB4tB0k27ghLPcACSpKht0HhEwBdWnLajM3MySKlWdYrcytdKnk2J'
BASE_URL = 'https://api.thecatapi.com/v1/images/search' #Base para acessar a API

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', Titulo = 'API Imagens')

@app.route('/cadastro')
def cadastro():
    acesso = {'x-api-key': API_KEY}  # acessa a nossa API, um dicionário
    solicitado = requests.get(BASE_URL, headers=acesso) # solicitação para a minha API colocando o acesso dentro da solicitação
    dados = solicitado.json() # recebendo os dados solicitados
    imagemdogato = dados[0]['url'] # pega uma url aleatória de um gato, filtra para pegar somente o link da imagem, lista de dicionário
    return render_template('cadastro.html', Titulo = 'API Imagens - Cadastro', imagem = imagemdogato)

@app.route('/galeria')
def galeria():
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('SELECT Descricao, Imagem FROM ImagensAPI')
    imagens = cursor.fetchall()
    return render_template('galeria.html', Titulo = 'API Imagens - Galeria', imagensbd = imagens)

@app.route('/criar', methods=['POST'])
def criar():
    imagem = request.form['url']
    descricao = request.form['descricao']
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('INSERT INTO ImagensAPI(Descricao,Imagem)'
                   'VALUES(?,?);'
                   '',(descricao,imagem))
    banco.commit()
    return redirect('/cadastro')

if __name__ == '__main__':
    app.run()
