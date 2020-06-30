import datetime

from random import random, randrange, seed

#Semente para configurar a geração de numeros aleatórios
valor = seed(datetime.time())
print(valor)

#Intervalo entre 0 e 1
aleatorio = random()
print(aleatorio)

#Mínimo = Inclusivo (entra na hora do sorteio)
#Máximo = Exclusivo (não entra na hora do sorteio)
intervalo = randrange(-10, 10)
print(intervalo)

for i in range(0, 20):
    intervalo = randrange(-10, 10)
    print(intervalo, end= ",")

