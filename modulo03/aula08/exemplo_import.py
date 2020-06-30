# AULA 08: MÓDULOS E PACOTES EXTERNOS
import math
import random

from math import pow, isfinite
potencia = pow(5, 3)
checarValor = isfinite(1)

print("Pontencia 5 e 3:", potencia)
print("isfinite:", checarValor)

print(math.isinf(1))
print(random.random())