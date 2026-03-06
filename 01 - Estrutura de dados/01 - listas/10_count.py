"""
Arquivo de Estudo: Método Count (.count) em Listas
Objetivo: Demonstrar como contabilizar o número de ocorrências de um 
          determinado elemento dentro de uma lista.
"""

# ==============================================================================
# Exemplo: Contando elementos com .count()
# ------------------------------------------------------------------------------
# Quando precisamos descobrir quantas vezes um valor específico se repete, o
# método '.count()' é a solução mais simples e performática. 
# 
# Ele iterará internamente de forma rápida e retornará um inteiro (int)
# informando exatamente quantas ocorrências daquele item foram encontradas.
# ==============================================================================

cores = ["vermelho", "azul", "verde", "azul"]

print("Ocorrências da cor 'vermelho':", cores.count("vermelho"))  # 1
print("Ocorrências da cor 'azul':", cores.count("azul"))          # 2
print("Ocorrências da cor 'verde':", cores.count("verde"))        # 1