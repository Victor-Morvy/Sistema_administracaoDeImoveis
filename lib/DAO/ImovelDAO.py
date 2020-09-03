import db.connection as database
import lib.funcoes as f


class ImovelDAO():
    def __init__(self):
        self.banco = database.BancoDeDados()

    def cadastrar_imovel(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"INSERT INTO imoveis(id_prop, logadrouro, complemento, numero, \
        bairro, cidade, cep, uf, observacao) values ('{obj.proprietario_id}', '{obj.logadrouro}', \
        '{obj.complemento}', '{obj.numero}', '{obj.bairro}', '{obj.cidade}', '{obj.cep}', \
        '{obj.uf}', '{obj.obs}')")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def alterar_imovel(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"UPDATE imoveis SET id_imovel = '{obj.id}', \
        id_prop = '{obj.proprietario_id}', logarouro = '{obj.logadrouro}', complemento = '{obj.complemento}', \
        numero = '{obj.numero}', bairro = '{obj.bairro}', cidade = '{obj.cidade}', cep = '{obj.cep}', \
        uf = '{obj.uf}', observacao = '{obj.obs}'\
        WHERE id_imovel = '{obj.id}'")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def excluir_imovel(self, obj):
        self.banco.conecta_db()
        self.banco.cursor.execute(f"DELETE FROM imoveis WHERE id_imovel = '{obj.id}'")

        try:
            self.banco.conn.commit()
            self.banco.desconecta_db()

        except ConnectionAbortedError:
            return False

        return True

    def listar_imoveis(self, tipo):
        self.banco.conecta_db()
        # todos imóveis
        if tipo == 0:
            self.query = "SELECT i.id_imovel, p.nome as proprietario, \
            i.logadrouro, i.numero, i.complemento, i.cep, i.bairro, \
            i.cidade, i.uf, i.observacao\
            FROM imoveis i\
            INNER JOIN proprietarios p on (i.id_prop = p.id_prop)"
        # imoveis alugados
        elif tipo == 1:
            self.query = "SELECT i.id_imovel, p.nome as proprietario, \
            i.logadrouro, i.numero, i.complemento, i.cep, i.bairro, \
            i.cidade, i.uf, i.observacao\
            FROM imoveis i\
            INNER JOIN proprietarios p on (i.id_prop = p.id_prop)\
            INNER JOIN contratos c on (c.imovel_id = i.id_imovel)"
        # imoveis disponíveis
        elif tipo == 2:
            self.query = "SELECT i.id_imovel, \
            p.nome as proprietario, i.logadrouro, i.numero, \
            i.complemento, i.cep, i.bairro, i.cidade, i.uf, i.observacao\
            FROM imoveis i\
            INNER JOIN proprietarios p on (i.id_prop = p.id_prop)\
            LEFT JOIN contratos c on (c.imovel_id = i.id_imovel)\
            WHERE c.imovel_id is null"

        self.banco.cursor.execute(self.query)
        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)

    def dados_imovel(self, obj):
        self.banco.conecta_db()

        self.banco.cursor.execute(f"SELECT * FROM imoveis WHERE id_imovel = '{obj.id}'")
        self.retorno = self.banco.cursor.fetchone()

        self.banco.desconecta_db()

        return list(self.retorno)

    def pesquisa_prop(self, tipo, valor):
        self.banco.conecta_db()

        if tipo == "Códgio":
            self.query = f"SELECT * FROM proprietarios WHERE id_prop = '{valor}'"
        elif tipo == "Nome":
            self.query = f"SELECT * FROM proprietarios WHERE nome LIKE '%{valor}%'"

        self.retorno = self.banco.cursor.fetchall()

        self.banco.desconecta_db()

        return f.tratar_resultado_banco(self.retorno)

