from lib.DTO.JanDTO import ProprietarioDTO
from lib.DAO.ProprietarioDAO import ProprietarioDAO

class ProprietarioCTR():
    def cadastrar_proprietario(self, nome, end, tel1, tel2, cpf, email, obs):
        proprietarioDTO = ProprietarioDTO()
        proprietarioDTO.nome = nome
        proprietarioDTO.endereco = end
        proprietarioDTO.tel1 = tel1
        proprietarioDTO.tel2 = tel2
        proprietarioDTO.cpf = cpf
        proprietarioDTO.email = email
        proprietarioDTO.obs = obs

        proprietarioDAO = ProprietarioDAO()
        proprietarioDAO.cadastrar_proprietario(proprietarioDTO)

    def dados_proprietario(self, id):
        proprietarioDAO = ProprietarioDAO()
        dados = proprietarioDAO.dados_proprietario(id)

        return dados

    def listar_proprietarios(self):
        pass

