alunos = {
    "nome": "Silvio",
    "sobrenome": "Dias Ferreira",
    "idade": 40,
    "endereco": "Rua das Cabras 125"
}

for aluno in alunos:
    #valoresAluno = alunos[aluno]
    #texto = aluno + ": "+ str(valoresAluno)
    #print(texto)
    print(aluno, ":", str(alunos[aluno]))

#Removendo elementos do dicionario com o comando del
del alunos["idade"]
print("\nApós remover a chave idade:")
for aluno in alunos:
    print(aluno, ":", str(alunos[aluno]))

print("\n", "Chaves:", alunos.keys())
print("\n", "Valores:", alunos.values())
print("\n", "Get Endereço:", alunos.get("endereco", None))

