from lib.DTO.JanDTO import ProprietarioDTO
from lib.DAO.ProprietarioDAO import ProprietarioDAO

class ProprietarioCTR():


    def cadastrar_proprietario(self, nome, end, tel1, tel2, cpf, email, obs):
        self.proprietarioDTO = ProprietarioDTO()
        self.proprietarioDTO.nome = nome
        self.proprietarioDTO.endereco = end
        self.proprietarioDTO.tel1 = tel1
        self.proprietarioDTO.tel2 = tel2
        self.proprietarioDTO.cpf = cpf
        self.proprietarioDTO.email = email
        self.proprietarioDTO.obs = obs

        self.proprietarioDAO = ProprietarioDAO()
        self.proprietarioDAO.cadastrar_proprietario(self.proprietarioDTO)

    def dados_proprietario(self, id):
        self.proprietarioDAO = ProprietarioDAO()
        self.dados = self.proprietarioDAO.dados_proprietario(id)

        return self.dados

    def listar_proprietarios(self):
        self.proprietarioDAO = ProprietarioDAO()
        return self.proprietarioDAO.listar_proprietarios()

    def excluir_proprietario(self, id):
        self.proprietarioDTO = ProprietarioDTO()
        self.proprietarioDTO.id = id

        self.proprietarioDAO = ProprietarioDAO()
        self.proprietarioDAO.excluir_proprietario(self.proprietarioDTO)

    def alterar_proprietario(self, id, nome, end, tel1, tel2, cpf, email, obs):
        self.proprietarioDTO = ProprietarioDTO()
        self.proprietarioDTO.id = id
        self.proprietarioDTO.nome = nome
        self.proprietarioDTO.endereco = end
        self.proprietarioDTO.tel1 = tel1
        self.proprietarioDTO.tel2 = tel2
        self.proprietarioDTO.cpf = cpf
        self.proprietarioDTO.email = email
        self.proprietarioDTO.obs = obs

        self.proprietarioDAO = ProprietarioDAO()
        self.proprietarioDAO.alterar_proprietario(self.proprietarioDTO)

