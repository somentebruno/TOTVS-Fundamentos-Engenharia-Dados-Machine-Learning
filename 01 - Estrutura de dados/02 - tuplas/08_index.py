"""
Arquivo de Estudo: Método .index() em Tuplas
Objetivo: Demonstrar como localizar a posição (índice) de um elemento
          específico dentro de uma tupla utilizando o método .index().
"""

# ==============================================================================
# Exemplo 1: Localizando Elementos com .index()
# ------------------------------------------------------------------------------
# O método .index(valor) percorre a tupla e retorna o índice (posição inteira)
# da PRIMEIRA ocorrência do 'valor' encontrado.
#
# Características importantes:
#   - Retorna apenas a posição da PRIMEIRA ocorrência, ignorando duplicatas.
#   - É case-sensitive: "Python" e "python" são considerados valores distintos.
#   - Lança uma exceção ValueError se o valor não existir na tupla.
#     Para evitar erros, é recomendado verificar antes com o operador 'in':
#     Ex: if "java" in linguagens: print(linguagens.index("java"))
# ==============================================================================
linguagens = ("python", "js", "c", "java", "csharp",)

# "java" está na posição 3 (quarto elemento, índice 0-based)
print(linguagens.index("java"))  # 3

# "python" está na posição 0 (primeiro elemento)
print(linguagens.index("python"))  # 0