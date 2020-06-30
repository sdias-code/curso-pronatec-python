# Retornando um valor

def exemplo(valor):
    resultado = None
    numero = valor * 2
    if numero > 10:
        resultado = numero
    else:
        resultado = valor + 5
    return resultado

opcao1 = exemplo(9)
print(opcao1)

opcao2 = exemplo(3)
print(opcao2)