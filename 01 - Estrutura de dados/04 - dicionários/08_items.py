"""
Arquivo de Estudo: Método .items() em Dicionários
Objetivo: Demonstrar como obter uma visão de todos os pares chave-valor de um 
          dicionário na forma de uma coleção de tuplas.
"""

# ==============================================================================
# Exemplo 1: Obtendo Pares Chave-Valor com .items()
# ------------------------------------------------------------------------------
# O método .items() retorna um objeto do tipo 'dict_items', que é uma visão 
# dinâmica dos itens do dicionário. Cada item é representado como uma tupla 
# no formato (chave, valor). 
# 
# Esta é a forma padrão e mais eficiente para iterar sobre dicionários 
# quando precisamos manipular a chave e o valor ao mesmo tempo.
# ==============================================================================
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Retorna uma visão dos pares (chave, valor)
resultado = contatos.items()
print(resultado)  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])