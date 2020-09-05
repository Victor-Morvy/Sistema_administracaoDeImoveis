import db.connection as database
import lib.funcoes as f

class ContaDAO():
    def __init__(self):
        self.banco = database.BancoDeDados()