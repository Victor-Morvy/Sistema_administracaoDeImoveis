import db.connection as database
import lib.funcoes as f


class ProprietarioDAO():

    def __init__(self):
        self.banco = database.BancoDeDados()

    def cadastrar_proprietario(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"INSERT INTO proprietarios(cpf, nome, telefone1, telefone2, endereco, email, observacao)\
                                  values('{obj.cpf}', '{obj.nome}', '{obj.tel1}',\
                                  '{obj.tel2}', '{obj.email}', '{obj.endereco}', '{obj.obs}')")
        self.banco.conn.commit()
        self.banco.desconecta_db()

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def alterar_proprietario(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"UPDATE proprietarios SET cpf = '{obj.cpf}', nome = '{obj.nome}', \
        telefone1 = '{obj.tel1}', telefone2 = '{obj.tel2}', endereco = '{obj.endereco}', email = '{obj.email}', observacao = '{obj.obs}'\
        WHERE id_prop = {obj.id}")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def excluir_proprietario(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"DETELE FROM proprietarios WHERE id_prop = {obj.id}")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def listar_proprietarios(self):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"SELECT * FROM proprietarios")
        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)

    def dados_proprietario(self, id):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"SELECT * FROM proprietarios WHERE id_prop = {id}")
        self.retorno = self.banco.cursor.fetchone()

        self.banco.desconecta_db()

        return list(self.retorno)
