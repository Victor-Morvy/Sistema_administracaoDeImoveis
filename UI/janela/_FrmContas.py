from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import lib.ColumnListview as multiList
import os
from lib.ValidEntry import validate_entry

class JanContas():

    def __init__(self):
        if self.jan == None:

            self.padInY = 5
            self.entryWidth = 58

            self.jan = Tk()

            self.validate = self.jan.register(validate_entry)

            #self.entt = validEntry.Valid_Entry(self.jan, 2)



            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_janela)
            self.janFrame = Frame(self.jan)
            self.janFrame.pack(side=LEFT, fill=X, anchor=NW, expand=True)

            self.lfJanelaDados = LabelFrame(self.janFrame, text=("Confirme a data:"))
            self.lfJanelaDados.pack(fill=X, anchor=NW, padx=3, pady=3)

            self.lfJanelaBtns = LabelFrame(self.janFrame)
            self.lfJanelaBtns.pack(fill=X, anchor=NW, padx=3, pady=3)

            self.diaIni = Entry(self.lfJanelaDados, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.diaIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)
            self.diaIni.focus_set()

            self.labelBarra = Label(self.lfJanelaDados, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.mesIni = Entry(self.lfJanelaDados, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.mesIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.labelBarra = Label(self.lfJanelaDados, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.anoIni = Entry(self.lfJanelaDados, width=5, validate="key", validatecommand=(self.validate, "%P", 4))
            self.anoIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.btnSalvar = Button(self.lfJanelaBtns, text="Salvar", width=10).pack(anchor=NW, padx=5, pady=5, side=LEFT)
            self.btnCancel = Button(self.lfJanelaBtns, text="Cancelar", width=10, command=self.fecha_janela).pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.jan.geometry("250x112+200+200")
            self.jan.title("Data")
            self.jan.iconbitmap(os.path.dirname(__file__) + '/../images/icon.ico')
            self.jan.resizable(0, 0)
        else:
            self.jan.lift()