import sqlite3
conexao = sqlite3.connect('API-Imagens.db')
cursor = conexao.cursor() # executar comando SQL
cursor.execute('CREATE TABLE IF NOT EXISTS ImagensAPI'
               '(ID INTEGER PRIMARY KEY,'
               'Descricao TEXT, Imagem TEXT)')
