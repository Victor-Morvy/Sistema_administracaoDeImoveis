import db.connection as database


class ProprietarioDAO():

    def cadastrar_proprietario(self, obj):
        self.banco = database.BancoDeDados()

        self.banco.cursor.execute(f"INSERT INTO proprietarios(cpf, nome, telefone1, telefone2, endereco, email, observacao)\
                                  values('{obj.cpf}', '{obj.nome}', '{obj.tel1}',\
                                  '{obj.tel2}', '{obj.email}', '{obj.endereco}', '{obj.obs}')")
        self.banco.conn.commit()
        self.banco.desconecta_db()

    def alterar_proprietario(self, obj):
        self.banco = database.BancoDeDados()

        self.banco.cursor.execute(f"UPDATE proprietarios SET cpf = '{obj.cpf}', nome = '{obj.nome}', \
        telefone1 = '{obj.tel1}', telefone2 = '{obj.tel2}', endereco = '{obj.endereco}', email = '{obj.email}', observacao = '{obj.obs}'\
        WHERE id_prop = {obj.id}")

        self.banco.conn.commit()
        self.banco.desconecta_db()

    def excluir_proprietario(self, obj):
        self.banco = database.BancoDeDados()

        self.banco.cursor.execute(f"DETELE FROM proprietarios id_prop = {obj.id}")

        self.banco.conn.commit()
        self.banco.desconecta_db()

    def listar_proprietarios(self):
        self.banco = database.BancoDeDados()

        self.banco.cursor.execute(f"SELECT * FROM proprietarios")
        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return self.retorno