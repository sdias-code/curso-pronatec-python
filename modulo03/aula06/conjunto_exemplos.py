# Criando conjuntos

reais = {1.0, 2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 7.5} #Criando um dicionario - {}
for n in reais:
    print(n)

inteiros = set([1, 2, 3, 4, 5, 6]) #Criando conjunto - set()

condicao1 = 3 in reais
print(condicao1)

condicao2 = 3 in inteiros
print(condicao2)

inteirosMenosReais = inteiros - reais # Inteiros que não estão nos reais.
print(inteirosMenosReais)

reaisMenosInteiros = reais - inteiros # Reais que não estão nos inteiros.
print(reaisMenosInteiros)

uniaoDoisConjuntos = reais | inteiros # Números que estão em um ou outro.
print(uniaoDoisConjuntos)

temDoisConjuntos = reais & inteiros # Números que estão nos dois conjuntos.
print(temDoisConjuntos)

numerosEmUmNaoNosDois = reais ^ inteiros # Números em um ou outro, mas não nos dois.
print(numerosEmUmNaoNosDois)


