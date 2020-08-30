import tkinter as tk

def validate_entry(valor, tam_maximo):
    valid = valor.isdigit() and len(valor) <= int(tam_maximo) or valor == ""
    return valid
