from tkinter import *

root = Tk()
root.geometry("300x200")

navbar = Frame(root, bg="green", width=100)
navbar.pack(anchor=W, fill=Y, expand=False, side=LEFT)  # <----

content_frame = Frame(root, bg="orange")
content_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )

root.mainloop()

class Imovel:

    def __init__(self):
        self.imo_id = None
        self.end = None
        self.numero = None
        self.bairro = None
        self.cidade = None
        self.uf = None
        self.proprietario = None

class Proprietario:

    def __init__(self):
        self.prop_id = None
        self.nome = None
        self.cpf = None
        self.tel1 = None
        self.tel2 = None
        self.end = None
        self.email = None

class Inquilino:

    def __init__(self):
        self.inq_id = None
        self.nome = None
        self.cpf = None
        self.tel1 = None
        self.tel2 = None
        self.email = None

