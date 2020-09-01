from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import lib.ColumnListview as multiList
import os
from lib.ValidEntry import validate_entry

class JanInquilino():

    def __init__(self):
        if self.jan == None:
            self.padInY = 5
            self.entryWidth = 58

            self.jan = Tk()

            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_janela)
            self.janFrame = Frame(self.jan)
            self.janFrame.pack(side=LEFT, fill=X, anchor=NW, expand=True)

            self.lfJanelaDados = LabelFrame(self.janFrame, text="Dados")
            self.lfJanelaDados.pack(fill=X, anchor=NW, padx=3, pady=3)

            self.lfJanelaBtns = LabelFrame(self.janFrame)
            self.lfJanelaBtns.pack(fill=X, anchor=NW, padx=3, pady=3)

            self.l1 = Label(self.lfJanelaDados, text="Nome:").grid(row=0, sticky=W, padx=5, pady=self.padInY)
            self.e1 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=0, column=1)

            self.l2 = Label(self.lfJanelaDados, text="Telefone 1:").grid(row=1, sticky=W, padx=5, pady=self.padInY)
            self.e2 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=1, column=1)

            self.l3 = Label(self.lfJanelaDados, text="Telefone 2:").grid(row=2, sticky=W, padx=5, pady=self.padInY)
            self.e3 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=2, column=1)

            self.l4 = Label(self.lfJanelaDados, text="CPF:").grid(row=3, sticky=W, padx=5, pady=self.padInY)
            self.e4 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=3, column=1)

            self.l5 = Label(self.lfJanelaDados, text="E-mail:").grid(row=4, sticky=W, padx=5, pady=self.padInY)
            self.e5 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=4, column=1)

            self.l6 = Label(self.lfJanelaDados, text="Observação:").grid(row=5, sticky=NW, padx=5, pady=self.padInY)
            self.e6 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=5, column=1)

            self.btnSalvar = Button(self.lfJanelaBtns, text="Salvar", width=10).pack(anchor=NW, padx=5, pady=5,
                                                                                     side=LEFT)
            self.btnCancel = Button(self.lfJanelaBtns, text="Cancelar", width=10, command=self.fecha_janela).pack(
                anchor=NW, padx=5, pady=5, side=LEFT)

            self.jan.geometry("520x277+200+200")
            self.jan.title("Inquilino")
            self.jan.iconbitmap(os.path.dirname(__file__) + '/../images/icon.ico')
            self.jan.resizable(0, 0)
        else:
            self.jan.lift()