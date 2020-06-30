import time
# Posso pegar a hora em segundos
hora = time.time()
print("Mostrar hora em segundos:", hora)

# Posso formatar como mostrar a data
hora_formatada = time.strftime("%H:%M:%S")
print("Hora formatada:", hora_formatada)

# Operações
hora = hora - 100
print("Operações:", hora)

diferenca = time.time() - hora
print("Diferença:", diferenca)
