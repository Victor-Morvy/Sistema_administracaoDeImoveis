'''
Data........: 2020-08-03
Projeto.....: Admin imobiliária
Arquivo.....: connection.py
Descrição...: Este módulo serve para conexões básicas ao banco de dados
Autor.......: Victor Hugo Martins de Oliveira
Observações.: 2020-08-03 - [R00] Criação do Arquivo - Versao 1.00
                2020-09-02 - conexão com o banco de dados
              ...
Referencias:
'''

import os
import sqlite3

class BancoDeDados():


    def conecta_db(self):
        try:

            self.conn = sqlite3.connect("imobiliaria_admin.db")
            self.cursor = self.conn.cursor()
            print("conexao estabelecida com sucesso")

            self.sqlite_select_Query = "select sqlite_version();"
            self.cursor.execute(self.sqlite_select_Query)
            record = self.cursor.fetchall()
            print("SQLite Database Version is: ", record)
            self.cursor.close()

        except:
            print("erro ao conectar no banco")

    def desconecta_db(self):
        self.conn.close()
