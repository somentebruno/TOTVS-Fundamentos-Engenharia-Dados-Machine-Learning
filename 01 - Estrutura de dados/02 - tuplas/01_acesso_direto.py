"""
Arquivo de Estudo: Acesso Direto em Tuplas
Objetivo: Demonstrar como acessar elementos individuais de uma tupla
          utilizando seus índices (posições).
"""

# ==============================================================================
# Exemplo 1: Acessando Elementos por Índice Positivo
# ------------------------------------------------------------------------------
# Assim como nas listas, as tuplas são coleções ordenadas e indexadas.
# Isso significa que cada elemento possui uma posição numérica fixa associada a ele.
# A contagem de índices padrão (positivos) sempre inicia no zero (0) para o
# primeiro elemento, e cresce da esquerda para a direita.
# A tentativa de acessar um índice além do tamanho da tupla causa IndexError.
# ==============================================================================
frutas = ("maçã", "laranja", "uva", "pera",)

# Acessa o primeiro elemento da tupla (índice 0)
print(frutas[0])  # maçã

# Acessa o terceiro elemento da tupla (índice 2)
print(frutas[2])  # uva