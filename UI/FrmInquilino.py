from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import lib.ColumnListview as multiList
import os

class FrmInquilino():

    def on_inq_select(self, data):
        self.selecionado = data[0]

    def janela_inquilino(self):
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

    def fecha_janela(self):
        if self.jan != None:
            self.jan.destroy()
            self.jan = None

    def __init__(self, conteudoFrame):
        self.selecionado = None

        self.jan = None

        self.frame = Frame(conteudoFrame)
        self.frame.pack(fill=BOTH, expand=TRUE)
        self.frame.propagate(0)

        #FRAME PROPRIETARIOS MULTILIST

        self.lfInqs = LabelFrame(self.frame, text="Inquilinos")
        self.lfInqs.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameInquilinos = Frame(self.lfInqs, bd=3, relief=SUNKEN)
        self.frameInquilinos.pack(anchor=NW, fill=X, pady=5, padx=5)

        self.inqMc = multiList.Multicolumn_Listbox(self.frameInquilinos, ["Código", "Nome", "Telefone 1", "Telefone 2", "CPF", "E-mail", "Observações"], stripped_rows=("black", "#f2f2f2"),
                                 command=self.on_inq_select, cell_anchor="w", heading_anchor=W)

        self.inqMc.configure_column(0, stretch=False, minwidth=65, width=65)
        self.inqMc.configure_column(1, stretch=False, minwidth=200, width=200)
        self.inqMc.configure_column(2, stretch=False, minwidth=120, width=120)
        self.inqMc.configure_column(3, stretch=False, minwidth=120, width=120)
        self.inqMc.configure_column(4, stretch=False, minwidth=120, width=120)
        self.inqMc.configure_column(5, stretch=False, minwidth=250, width=250)
        self.inqMc.configure_column(6, stretch=False, minwidth=550, width=550)

        self.verscrollbar = ttk.Scrollbar(self.frameInquilinos, orient="vertical", command=self.inqMc.interior.yview)

        self.xScrollBar = ttk.Scrollbar(self.frameInquilinos, orient="horizontal", command=self.inqMc.interior.xview)

        self.verscrollbar.pack(side="right", fill="y")
        self.xScrollBar.pack(side="bottom", fill=X)

        #propMc.interior.columnconfigure()
        self.inqMc.interior.config(yscrollcommand=self.verscrollbar.set, xscrollcommand=self.xScrollBar.set)

        self.inqMc.interior.pack(fill=X, expand=True)

        #FRAME BOTÕES
        self.lfBtns = LabelFrame(self.frame)
        self.lfBtns.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameButton = Frame(self.lfBtns)
        self.frameButton.pack(anchor=NW, padx=5, pady=5, fill=X)

        self.button_novo = Button(self.frameButton, text="Novo Inquilino", command=self.janela_inquilino)
        self.button_novo.pack(side=LEFT, padx=5)

        self.button_editar = Button(self.frameButton, text="Alterar Inquilino")
        self.button_editar.pack(side=LEFT, padx=5)

        self.button_excluir = Button(self.frameButton, text="Excluir Inquilino")
        self.button_excluir.pack(side=LEFT, padx=5)



