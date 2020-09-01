class ProprietarioDTO():
    def __init__(self):
        self.id = None
        self.nome = None
        self.endereco = None
        self.tel1 = None
        self.tel2 = None
        self.CPF = None
        self.email = None
        self.obs = None

class InquilinoDTO():
    def __init__(self):
        self.id = None
        self.nome = None
        self.tel1 = None
        self.tel2 = None
        self.CPF = None
        self.email = None
        self.obs = None

class ImovelDTO():
    def __init__(self):
        self.id = None
        self.proprietario_id = None
        self.logradouro = None
        self.numero = None
        self.bairro = None
        self.cidade = None
        self.uf = None
        self.obs = None

class ContratoDTO():
    def __init__(self):
        self.id = None
        self.inquilino_id = None
        self.imovel_id = None
        self.data_inicial = None
        self.data_final = None
        self.dia_pagamento = None
        self.val_aluguel = None
        self.admin_porcento = None
        self.garantia = None
        self.conta_agua = None
        self.conta_energia = None
        self.obs = None
