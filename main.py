from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import os
import UI.FmrInquilino as frmInq
import UI.FmrProprietario as frmProp
import UI.FrmImoveis as frmImo
import lib.ColumnListview as multiList

conteudoFrame = None
selectedModulo = "INICIO"


def destroyFrame():
    global conteudoFrame
    if conteudoFrame is not None:
        conteudoFrame.destroy()
        conteudoFrame = None

root = Tk()
caixa = Frame(root, bd=3, relief=SUNKEN)
caixa.pack(anchor=NW, fill=X)

def criaConteudoFrame(nome):
    global selectedModulo
    selectedModulo = nome
    destroyFrame()
    global root
    global conteudoFrame
    conteudoFrame = Frame(root, bd=5, relief=SUNKEN)
    conteudoFrame.pack(anchor=NW, fill=BOTH, expand=True, side="left")

def abrir_inq():
    criaConteudoFrame("INQUILINOS")
    global conteudoFrame
    frm_Inq = frmInq.FmrInquilino(conteudoFrame)
    frm_Inq.inqMc.table_data =[[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"]]
    frm_Inq.inqMc.configure_column(0, stretch=False, minwidth=65, width=65)
    frm_Inq.inqMc.configure_column(1, stretch=False, minwidth=200, width=200)
    frm_Inq.inqMc.configure_column(2, stretch=False, minwidth=120, width=120)
    frm_Inq.inqMc.configure_column(3, stretch=False, minwidth=120, width=120)
    frm_Inq.inqMc.configure_column(4, stretch=False, minwidth=120, width=120)
    frm_Inq.inqMc.configure_column(5, stretch=False, minwidth=250, width=250)
    frm_Inq.inqMc.configure_column(6, stretch=False, minwidth=550, width=550)
    btn_clicked()

def abrir_prop():
    criaConteudoFrame("PROPRIETARIOS")
    global conteudoFrame
    frm_prop = frmProp.FmrProprietario(conteudoFrame)
    frm_prop.propMc.table_data = [[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"]]
    #frm_prop.propMc.table_data =[["Ut volutpat nisl nec quam vestibulum",2,3,4,5,6],[1,2,3,4,5,6],[1,2,"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec leo erat, venenatis et nisl et, bibendum convallis massa. Sed et est id ipsum malesuada volutpat eu auctor sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam erat risus, tristique nec bibendum at, tempor a lacus.",4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
    frm_prop.propMc.configure_column(0, stretch=False, minwidth=65, width=65)
    frm_prop.propMc.configure_column(1, stretch=False, minwidth=200, width=200)
    frm_prop.propMc.configure_column(2, stretch=False, minwidth=350, width=350)
    frm_prop.propMc.configure_column(3, stretch=False, minwidth=120, width=120)
    frm_prop.propMc.configure_column(4, stretch=False, minwidth=120, width=120)
    frm_prop.propMc.configure_column(5, stretch=False, minwidth=120, width=120)
    frm_prop.propMc.configure_column(6, stretch=False, minwidth=250, width=250)
    frm_prop.propMc.configure_column(7, stretch=False, minwidth=550, width=550)
    btn_clicked()

def abrir_imo():
    criaConteudoFrame("IMOVEIS")
    global conteudoFrame
    frm_imovel = frmImo.FrmImoveis(conteudoFrame)
    frm_imovel.inqMc.table_data = [[1,
                                    "Vilma Barbosa de Oliveira",
                                    "Rua das Andorinhas Amargas",
                                    2290,
                                    "Jardim Nova Palmares Okay",
                                    "Vale do Sul",
                                    "SP",
                                    "1546654786541321",
                                    "4946516516516541",
                                    "Casa a, frente para a Rua bla bla bla"]]
    frm_imovel.inqMc.configure_column(0, stretch=False, minwidth=65, width=65)
    frm_imovel.inqMc.configure_column(1, stretch=False, minwidth=200, width=200)
    frm_imovel.inqMc.configure_column(2, stretch=False, minwidth=250, width=250)
    frm_imovel.inqMc.configure_column(3, stretch=False, minwidth=65, width=65)
    frm_imovel.inqMc.configure_column(4, stretch=False, minwidth=200, width=200)
    frm_imovel.inqMc.configure_column(5, stretch=False, minwidth=120, width=120)
    frm_imovel.inqMc.configure_column(6, stretch=False, minwidth=30, width=30)
    frm_imovel.inqMc.configure_column(7, stretch=False, minwidth=150, width=150)
    frm_imovel.inqMc.configure_column(8, stretch=False, minwidth=150, width=150)
    frm_imovel.inqMc.configure_column(9, stretch=False, minwidth=550, width=550)
    btn_clicked()

def abrir_contrato():
    criaConteudoFrame("CONTRATOS")
    btn_clicked()

def abrir_conta():
    criaConteudoFrame("CONTAS")
    btn_clicked()

zoomImage = 2

imgInq = PhotoImage(file=os.path.dirname(__file__) + "/images/inquilino.png").subsample(zoomImage)
imgProp = PhotoImage(file=os.path.dirname(__file__) + "/images/proprietario.png").subsample(zoomImage)
imgImovel = PhotoImage(file=os.path.dirname(__file__) + "/images/imovel.png").subsample(zoomImage)
imgContrato = PhotoImage(file=os.path.dirname(__file__) + "/images/contrato.png").subsample(zoomImage)
imgContas = PhotoImage(file=os.path.dirname(__file__) + "/images/contas.png").subsample(zoomImage)

tamBotao = 100

bProp = Button(caixa, text="Proprietários", image=imgProp, compound="top", width=tamBotao, command=abrir_prop)
bProp.pack(side="left")

bInq = Button(caixa, text="Inquilinos", image=imgInq, compound="top", width=tamBotao, command=abrir_inq)
bInq.pack(side="left")

bImo = Button(caixa, text="Imoveis", image=imgImovel, compound="top", width=tamBotao, command=abrir_imo)
bImo.pack(side="left")

bContrato = Button(caixa, text="Contratos", image=imgContrato, compound="top", width=tamBotao, command=abrir_contrato)
bContrato.pack(side="left")

bConta = Button(caixa, text="Contas", image=imgContas, compound="top", width=tamBotao, command=abrir_conta)
bConta.pack(side="left")
destroyFrame()
conteudoFrame = Frame(root, bd=5, relief=SUNKEN)
conteudoFrame.pack(anchor=NW, fill=BOTH, expand=True, side="left")

labelTitulo = Label(conteudoFrame, text="GERENCIAMENTO DE ALUGUEL BLABABALBABASKDSD", font="Arial 25")
labelTitulo.pack(anchor=NW)
'''
labelTitulo2 = Label(conteudoFrame, text="GERENCIAMENTO DE ALUGUEL BLABABALBABASKDSD", font="Arial 25")
labelTitulo2.pack(anchor=NW)
labelTitulo3 = Label(conteudoFrame, text="GERENCIAMENTO DE ALUGUEL BLABABALBABASKDSD", font="Arial 25")
labelTitulo3.pack(anchor=NW)
labelTitulo4 = Label(conteudoFrame, text="GERENCIAMENTO DE ALUGUEL BLABABALBABASKDSD", font="Arial 25")
labelTitulo4.pack(anchor=NW)'''

def btn_clicked():
    global selectedModulo

    bInq.config(relief=RAISED)
    bProp.config(relief=RAISED)
    bConta.config(relief=RAISED)
    bImo.config(relief=RAISED)
    bContrato.config(relief=RAISED)

    if selectedModulo == "INQUILINOS":
        bInq.config(relief=SUNKEN)

    elif selectedModulo == "PROPRIETARIOS":
        bProp.config(relief=SUNKEN)

    elif selectedModulo == "IMOVEIS":
        bImo.config(relief=SUNKEN)

    elif selectedModulo == "CONTRATOS":
        bContrato.config(relief=SUNKEN)

    elif selectedModulo == "CONTAS":
        bConta.config(relief=SUNKEN)

#yScrollBar.config(command=conteudoFrame.)
root.iconbitmap(os.path.dirname(__file__) + '/images/icon.ico')
root.geometry("800x600")
root.title("Administração de locação")
root.state("zoomed")
root.minsize(1024,768)

root.mainloop()

