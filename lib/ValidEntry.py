def validate_entry(valor, tam_maximo):
    valid = valor.isdigit() and len(valor) <= int(tam_maximo) or valor == ""
    return valid

def number_entry(valor):
    valid = valor.isdigit() or valor == ""
    return valid