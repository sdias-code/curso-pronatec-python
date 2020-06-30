import numpy as np
import matplotlib.pyplot as plt
from random import randrange

# Descrição do gráfico
# Gráfico de barras
# Pontos por time em cada esporte
# Mostrar o nome de cada esporte => Labels
# Para mostar pontos para cada time teremos subgraficos

time1_nome = "Azul"
time2_nome = "Laranja"

nome_esportes = ["Futebol", "Handball", "Volei", "Basquete", "Baseball"] #labels
pontuacao_azul = [randrange(0, 10),
                  randrange(0, 10),
                  randrange(0, 10),
                  randrange(0, 10),
                  randrange(0, 10)]

pontuacao_laranja = [randrange(0, 10),
                     randrange(0, 10),
                     randrange(0, 10),
                     randrange(0, 10),
                     randrange(0, 10)]

esportes = np.arange(len(nome_esportes))
largura = 0.30
figura, eixos = plt.subplots()

# barras ficam nos eixos e são do tipo "barra" => eixos.bar()
# parametros das barras = posição, valores, largura, título
barra_azul = eixos.bar(esportes - (largura/2), pontuacao_azul, largura, label=time1_nome)
barra_laranja = eixos.bar(esportes + (largura/2), pontuacao_laranja, largura, label=time2_nome)

# Textos nos eixos
eixos.set_ylabel("Pontuação no Esporte")
eixos.set_xlabel("Modalidade do Esporte")
eixos.set_title("Pontuação da Gincana")
eixos.set_xticks(esportes)
eixos.set_xticklabels(nome_esportes)
eixos.legend()

figura.tight_layout()
plt.show()
