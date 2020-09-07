import db.connection as database
import lib.funcoes as f

class ContaDAO():
    def __init__(self):
        self.banco = database.BancoDeDados()

    def listar_contratos(self):
        self.banco.conecta_db()

        self.banco.cursor.execute("SELECT * FROM contratos")

        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)

    def listar_boletos(self, tipo, contrato_id):
        self.banco.conecta_db()

        if tipo == 0:
            self.query = f"SELECT * from contas WHERE data_pagamento is NULL and contrato_id = {contrato_id}"

        elif tipo == 1:
            self.query = f"SELECT * from contas WHERE contrato_id = {contrato_id}"

        elif tipo == 2:
            self.query = f"SELECT * from contas WHERE data_pagamento is not NULL and contrato_id = {contrato_id}"

        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)

    def dados_boleto(self, id):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"SELECT * FROM contas WHERE conta_id = '{id}'")
        self.retorno = self.banco.cursor.fetchone()

        self.banco.desconecta_db()

        return list(self.retorno)

    def cadastrar_conta(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"INSERT INTO contas(contrato_id, tipo, valor_pago, \
                mes_referente, data_envio, data_pagamento, data_vencimento, observacao) values ('\
                '{obj.contrato_id}', '{obj.tipo}', '{obj.valor_pago}', '{obj.mes_de_referencia}', '{obj.data_de_envio}',\
                '{obj.data_de_pagamento}', '{obj.data_de_vencimento}', '{obj.obs}')")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def alterar_conta(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"UPDATE contas SET\
        contrato_id = '{obj.contrato_id}',\
        tipo = '{obj.tipo}',\
        valor_pago = '{obj.valor_pago}',\
        mes_referente = '{obj.mes_de_referencia}',\
        data_envio = '{obj.data_de_envio}',\
        data_pagamento = '{obj.data_de_pagamento}',\
        data_vencimento = '{obj.data_de_vencimento}',\
        observacao = '{obj.obs}'\
        WHERE conta_id = '{obj.id}'\
        ")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def excluir_conta(self, obj):
        self.banco.conecta_db()
        self.banco.cursor.execute(f"DELETE FROM contas WHERE conta_id = '{obj.id}'")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True