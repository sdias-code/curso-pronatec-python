# Estrutura de condição IF-ELIF-ELSE
idade = int(input("Digite sua idade:"))
if idade >= 10 and idade < 20:
    print("Você é adolecente")
elif idade >= 20 and idade < 30:
    print("Você é jovem")
elif idade >= 30 and idade <= 100:
    print("Você é adulto")
else:
    print("Valor não encontrado!")
