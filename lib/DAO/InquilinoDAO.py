import db.connection as database
import lib.funcoes as f

class InquilinoDAO():

    def cadastrar_inquilino(self, obj):
        self.banco = database.BancoDeDados()

        self.banco.cursor.execute(f"INSERT INTO inquilinos(cpf, nome, telefone1, telefone2, email, observacao)\
                                  values('{obj.cpf}', '{obj.nome}', '{obj.tel1}',\
                                  '{obj.tel2}', '{obj.email}', '{obj.obs}')")
        self.banco.conn.commit()
        self.banco.desconecta_db()

    def alterar_inquilino(self, obj):
        self.banco = database.BancoDeDados()

        self.banco.cursor.execute(f"UPDATE inquilinos SET cpf = '{obj.cpf}', nome = '{obj.nome}', \
        telefone1 = '{obj.tel1}', telefone2 = '{obj.tel2}', email = '{obj.email}', observacao = '{obj.obs}'\
        WHERE id_inq = {obj.id}")

        self.banco.conn.commit()
        self.banco.desconecta_db()

    def excluir_inquilino(self, obj):
        self.banco = database.BancoDeDados()

        self.banco.cursor.execute(f"DETELE FROM inquilinos id_inq = {obj.id}")

        self.banco.conn.commit()
        self.banco.desconecta_db()

    def listar_inquilinos(self):
        self.banco = database.BancoDeDados()

        self.banco.cursor.execute(f"SELECT * FROM inquilinos")
        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)