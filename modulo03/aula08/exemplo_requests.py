import requests

# Vamos acessar um site
resposta = requests.get("https://google.com")

# Status Code => Informa qual o tipo de resposta
# 200 => Deu Certo
# 404 => Not Found
print("Status:\n", resposta.status_code)

# Verificar o encoding
print("\nEnconding:\n", resposta.encoding)

# Pegar os cabeçalhos (Headers)
print("\nCabeçalhos:\n", resposta.headers)

# Pegar o conteúdo (Content)
print("\nConteúdo:\n", resposta.content)
