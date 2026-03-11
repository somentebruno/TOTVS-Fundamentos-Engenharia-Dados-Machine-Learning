"""
Arquivo de Estudo: Função len() em Conjuntos
Objetivo: Demonstrar como obter o número total de elementos únicos de um conjunto,
          reforçando a eliminação automática de duplicatas pelos sets.
"""

# ==============================================================================
# Exemplo 1: Contando Elementos Únicos com len()
# ------------------------------------------------------------------------------
# A função built-in len() retorna um inteiro com o número de elementos 
# presentes no conjunto. Como sets eliminam duplicatas automaticamente,
# o resultado reflete apenas os valores únicos — não a quantidade total
# de itens passados na criação.
#
# Neste exemplo:
#   Valores passados: {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0} → 13 itens
#   Valores únicos:  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}           → 10 itens
#
# Características:
#   - Operação O(1): extremamente eficiente, o tamanho é armazenado internamente.
#   - Funciona com qualquer tipo de coleção: listas, tuplas, strings, sets, etc.
# ==============================================================================
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# Retorna 10: apenas os elementos únicos são contados
print(len(numeros))  # 10