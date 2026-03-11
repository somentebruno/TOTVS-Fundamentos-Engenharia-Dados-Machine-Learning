"""
Arquivo de Estudo: Matrizes (Tuplas Aninhadas)
Objetivo: Demonstrar a criação e o acesso de elementos em matrizes,
          utilizando tuplas dentro de tuplas (tuplas bidimensionais).
"""

# ==============================================================================
# Exemplo 1: Declarando e Acessando Matrizes com Tuplas
# ------------------------------------------------------------------------------
# Matrizes podem ser estruturadas aninhando coleções. No caso de tuplas,
# podemos criar uma tupla que contém outras tuplas como elementos.
# Para acessar um valor específico, usamos múltiplos índices [linha][coluna],
# onde o primeiro índice seleciona a tupla interna e o segundo acessa 
# o elemento dentro dessa tupla interna. Índices negativos também funcionam!
# ==============================================================================
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

# Acessa a primeira linha inteira (índice 0)
print(matriz[0])  # (1, "a", 2)

# Acessa a primeira linha (0) e, dentro dela, o primeiro elemento (0)
print(matriz[0][0])  # 1

# Acessa a primeira linha (0) e, dentro dela, o último elemento (-1)
print(matriz[0][-1])  # 2

# Acessa a última linha (-1) e, dentro dela, o último elemento (-1)
print(matriz[-1][-1])  # "c"