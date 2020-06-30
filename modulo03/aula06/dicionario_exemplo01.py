pessoa ={
    "nome": "Marta",
    "sobrenome": "Rocha",
    "idade": 40
}
print(pessoa)

print(pessoa["nome"])
print(pessoa["sobrenome"])
print(pessoa["idade"])

pessoa["sobrenome"] = "Dias Ferreira"
print(pessoa)

cpf = pessoa.get("cpf", None)
print(cpf)

print("\nRetornando as chaves de uma lista:")
chaves = pessoa.keys() # Retorna todas as chaves de uma lista
for chave in chaves:
    print(chave)

print("\nRetornando os valores de uma lista:")
valores = pessoa.values()
for valor in valores:
    print(valor)

print("\nRetornando lista personalizada")
chaves = pessoa.keys()
for chave in chaves:
    valor = pessoa[chave]
    texto = chave + ": " + str(valor)
    print(texto)

