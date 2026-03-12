"""
Arquivo de Estudo: Acessando Dados em Conjuntos (Sets)
Objetivo: Demonstrar que conjuntos não suportam acesso por índice e como
          contornar essa limitação convertendo o conjunto para lista.
"""

# ==============================================================================
# Exemplo 1: Acesso por Índice via Conversão para Lista
# ------------------------------------------------------------------------------
# Como conjuntos são NÃO indexados, não é possível acessar seus elementos
# diretamente por posição (ex: numeros[0] em um set lança TypeError).
#
# A alternativa mais comum é converter o conjunto para lista com list(),
# tornando a coleção indexável. Porém, atenção:
#   - A ordem dos elementos em um conjunto não é garantida.
#   - Ao converter para lista, a posição de cada elemento pode variar
#     entre execuções diferentes do programa.
#   - Para iteração sem necessidade de índice, use diretamente o 'for'.
# ==============================================================================
numeros = {1, 2, 3, 2}  # O valor 2 duplicado é automaticamente removido

# Converte o conjunto para lista, tornando-o indexável
numeros = list(numeros)

# Acessa o primeiro elemento da lista resultante (ordem pode variar!)
print(numeros[0])