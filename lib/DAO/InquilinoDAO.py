import db.connection as database
import lib.funcoes as f

class InquilinoDAO():

    def __init__(self):
        self.banco = database.BancoDeDados()

    def cadastrar_inquilino(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"INSERT INTO inquilinos(cpf, nome, telefone1, telefone2, email, observacao)\
                                  values('{obj.cpf}', '{obj.nome}', '{obj.tel1}',\
                                  '{obj.tel2}', '{obj.email}', '{obj.obs}')")
        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def alterar_inquilino(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"UPDATE inquilinos SET cpf = '{obj.cpf}', nome = '{obj.nome}', \
        telefone1 = '{obj.tel1}', telefone2 = '{obj.tel2}', email = '{obj.email}', observacao = '{obj.obs}'\
        WHERE id_inq = {obj.id}")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def excluir_inquilino(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"DETELE FROM inquilinos WHERE id_inq = {obj.id}")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def listar_inquilinos(self):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"SELECT * FROM inquilinos")
        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)

    def dados_inquilino(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"SELECT * FROM inquilinos WHERE id_inq = {obj.id}")
        self.retorno = self.banco.cursor.fetchone()

        self.banco.desconecta_db()

        return list(self.retorno)