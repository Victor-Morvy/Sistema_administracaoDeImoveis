from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import webbrowser
import lib.ColumnListview as multiList
import os

class Inicio():

    def on_select(self, data):
        print("called command when row is selected")
        print(data)
        print("\n")

    def callback(self, url):
        webbrowser.open_new(url)

    def __init__(self, conteudoFrame):
        self.filtroConta = IntVar()

        self.frame = Frame(conteudoFrame)
        self.frame.pack(fill=BOTH, expand=TRUE, anchor=NW)
        self.frame.propagate(0)

        self.frameInicio = Frame(self.frame)
        self.frameInicio.pack(anchor=NW, fill=X)

        # FRAMES DE INICIO
        self.padGeralX = 10
        self.padGeralY = 5

        self.fTitulo = Frame(self.frameInicio)
        self.fTitulo.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY, fill=X, expand=TRUE)
        self.labelTitulo = Label(self.fTitulo, text="ADMINISTRAÇÃO DE ALUGUEL DE IMÓVEIS", font="Arial 30")
        self.labelTitulo.pack(anchor=NW, padx=self.padGeralX-10, pady=self.padGeralY)

        self.fDescricao = Frame(self.frameInicio)
        self.fDescricao.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY, fill=X, expand=TRUE)
        self.lDescricao = Label(self.fDescricao, text="-Navegue pelo menu acima-\nCaso queira relatar algo sobre o software, favor reportar no e-mail abaixo com o assunto \"(Tkinter) - Admin de aluguel\".", font="Arial 9", justify=LEFT, fg="red")
        self.lDescricao.pack(anchor=NW, padx=self.padGeralX-10)

        self.fVersao = LabelFrame(self.frameInicio, text="Versão:")
        self.fVersao.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY, fill=X, expand=TRUE)
        self.lversao = Label(self.fVersao, text="v1.0", font="Arial 12")
        self.lversao.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY)

        self.fCriador = LabelFrame(self.frameInicio, text="Criador:")
        self.fCriador.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY, fill=X, expand=TRUE)
        self.lCriador = Label(self.fCriador, text="Victor Hugo Martins de Oliveira - Morvy", font="Arial 12")
        self.lCriador.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY)

        self.fEmail = LabelFrame(self.frameInicio, text="E-mail:")
        self.fEmail.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY, fill=X, expand=TRUE)
        self.eEmail = Entry(self.fEmail, relief="flat", bd=0, takefocus=0, highlightthickness=0, width=35, font="Arial 12")
        self.eEmail.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY)
        self.eEmail.insert('end', 'victorhugomartins28@gmail.com')
        self.eEmail.config(state="readonly")

        self.fGithub = LabelFrame(self.frameInicio, text="Repositório do projeto:")
        self.fGithub.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY, fill=X, expand=TRUE)
        self.lGithub = Label(self.fGithub, text="https://github.com/Victor-Morvy/Sistema_administracaoDeImoveis", font="Arial 12", fg="blue", cursor="hand2")
        self.lGithub.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY)
        self.lGithub.bind("<Button-1>", lambda e: self.callback("https://github.com/Victor-Morvy/Sistema_administracaoDeImoveis"))

        self.fLicensa = LabelFrame(self.frameInicio, text="Licensa de uso:")
        self.fLicensa.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY, fill=X, expand=TRUE)
        self.lLicensa = Label(self.fLicensa, text="Software Livre", font="Arial 12")
        self.lLicensa.pack(anchor=NW, padx=self.padGeralX, pady=self.padGeralY)





