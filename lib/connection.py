'''
Data........: 2020-08-03
Projeto.....: Admin imobiliária
Arquivo.....: connection.py
Descrição...: Este módulo serve para conexões básicas ao banco de dados
Autor.......: Victor Hugo Martins de Oliveira
Observações.: 2020-08-03 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias:
'''

import os
import sqlite3

#Definindo local da db
fileDB = os.path.dirname(__file__) + "/db/imobiliaria_admin.sqlite"
print("teste:" + url.split("/")[-1])

#Verifica se o arquivo do banco existe
print("Conectando db...")
if not os.path.exists(fileDB):
    print(f"O arquivo {fileDB} não existe!")
    exit(-1)
else:
    pass

#criando a base de dados
connection = sqlite3.connect(fileDB)

#get Cursor
cursor = connection.cursor()