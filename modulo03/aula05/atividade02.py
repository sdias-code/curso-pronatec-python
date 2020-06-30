# Você deve criar um programa para verificar se o aluno
# passou ou não de uma disciplina. Nesta escola a nota
# vai de 0 a 100.

nota_alunao = int(input("Entre com sua nota de 0 a 100: "))
if nota_alunao < 30:
    print("Aluno: REPROVADO!")
elif nota_alunao < 50:
    print("Aluno: RECUPERAÇÃO!")
else:
    print("Aluno: APROVADO!")
