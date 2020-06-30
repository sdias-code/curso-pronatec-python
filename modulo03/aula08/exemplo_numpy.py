import numpy as np

# Vetor = sequencia de elementos
# Arange = Popular meu vetor

vetor = np.arange(1, 21)
print("Vetor:", vetor)

# Criar uma matriz
# Reshape => Mudar o formato
# 4 linhas x 5 colunas = 4 * 5 = 20
matriz = vetor.reshape(4, 5)
print("Matriz:\n", matriz)

# Mostrar dimensões
dim = vetor.ndim
print("Dimensões:",dim)

print("Multiplicação x2:", (vetor * 2))
print("Adição:", vetor + 2)
print("Subtração:", (vetor -2))
print("Divisão:", (vetor / 2))

vetor_3d = np.ones((3, 4, 5))
print(vetor_3d)

