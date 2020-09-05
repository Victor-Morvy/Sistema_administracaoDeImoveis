import db.connection as database
import lib.funcoes as f

class ContratoDAO():
    def __init__(self):
        self.banco = database.BancoDeDados()

    def cadastrar_contrato(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"INSERT INTO contratos(imovel_id, inquilino_id, data_inicial_contrato,\
        data_final_contrato, valor_aluguel_contrato, porcent_admin, garantia, conta_energia_num,\
        conta_agua_num, observacao, dia_pagamento) values ('{obj.imovel_id}', '{obj.inquilino_id}', '{obj.data_inicial}',\
        '{obj.data_final}', '{obj.val_aluguel}', '{obj.admin_porcento}', '{obj.garantia}', '{obj.conta_energia}'\
        '{obj.conta_agua}', '{obj.obs}', '{obj.dia_pagamento}')")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def alterar_contrato(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"UPDATE contratos SET\
        imovel_id = '{obj.imovel_id}',\
        inquilino_id = '{obj.inquilino_id}',\
        data_inicial_contrato = '{obj.data_inicial}',\
        data_final_contrato = '{obj.data_final}',\
        valor_aluguel_contrato = '{obj.val_aluguel}',\
        porcent_admin = '{obj.admin_porcento}',\
        garantia = '{obj.garantia}',\
        conta_energia_num = '{obj.conta_energia}',\
        conta_agua_num = '{obj.conta_agua}',\
        observacao = '{obj.obs}',\
        dia_pagamento = '{obj.dia_pagamento}'\
        WHERE contrato_id = '{obj.id}'")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def excluir_contrato(self, obj):
        self.banco.conecta_db()
        self.banco.cursor.execute(f"DELETE FROM contratos WHERE contrato_id = '{obj.id}'")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def listar_contratos(self):
        self.banco.conecta_db()

        self.banco.cursor.execute("SELECT * FROM contratos")

        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)

    def dados_contrato(self, id):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"SELECT * FROM contratos WHERE contrato_id = '{id}'")
        self.retorno = self.banco.cursor.fetchone()

        self.banco.desconecta_db()

        return list(self.retorno)

    def pesquisa_inquilino(self, tipo, valor):
        self.banco.conecta_db()
        if tipo == "Códgio":
            self.query = f"SELECT * FROM inquilinos WHERE id_inq = '{valor}'"
        elif tipo == "Nome":
            self.query = f"SELECT * FROM inquilinos WHERE nome LIKE '%{valor}%'"

        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)

    def pesquisa_imovel(self, tipo, valor):
        self.banco.conecta_db()
        if tipo == "Códgio":
            self.query = f"SELECT * FROM imoveis WHERE id_imovel = '{valor}'"
        elif tipo == "Nome":
            self.query = f"SELECT *\
            FROM imoveis i\
            INNER JOIN proprietarios p on (p.id_prop = i.id_prop)\
            WHERE p.nome LIKE '%{valor}%'"

        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)
