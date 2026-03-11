"""
Arquivo de Estudo: Iteração em Dicionários
Objetivo: Demonstrar as diferentes formas de percorrer chaves e valores em 
          dicionários, utilizando loops simples e o método .items().
"""

# ==============================================================================
# Exemplo 1: Iteração Simples sobre as Chaves
# ------------------------------------------------------------------------------
# Por padrão, ao iterar diretamente sobre um dicionário, o Python percorre suas 
# CHAVES. Para obter o valor correspondente, usamos a chave recuperada para 
# acessar o dicionário (dict[chave]).
# ==============================================================================
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

# ==============================================================================
# Exemplo 2: Iteração com o Método .items()
# ------------------------------------------------------------------------------
# O método .items() é a forma mais pythônica de iterar quando precisamos de 
# ambos: chave e valor. Ele retorna uma visão de tuplas (chave, valor), 
# permitindo o desempacotamento direto nas variáveis do loop.
# ==============================================================================
for chave, valor in contatos.items():
    print(chave, valor)