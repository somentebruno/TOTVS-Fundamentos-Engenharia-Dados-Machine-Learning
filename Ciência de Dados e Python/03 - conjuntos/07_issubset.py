"""
Arquivo de Estudo: Método .issubset() em Conjuntos
Objetivo: Demonstrar como verificar se todos os elementos de um conjunto
          estão contidos dentro de outro conjunto.
"""

# ==============================================================================
# Exemplo 1: Verificando Subconjunto com .issubset()
# ------------------------------------------------------------------------------
# O método .issubset() retorna True se TODOS os elementos do conjunto chamador
# estiverem presentes no conjunto passado como argumento. Caso contrário,
# retorna False.
#
# Em termos matemáticos: A ⊆ B (A é subconjunto de B)
# significa que todo elemento de A também pertence a B.
#
# Características importantes:
#   - É uma verificação booleana (retorna True ou False).
#   - Equivalente ao operador <=: conjunto_a <= conjunto_b.
#   - Um conjunto é sempre subconjunto de si mesmo (A.issubset(A) → True).
#   - O conjunto vazio set() é subconjunto de qualquer conjunto.
#   - Não confundir com .issuperset(), que verifica a relação inversa.
# ==============================================================================
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# A ⊆ B → True: todos os elementos de A (1, 2, 3) estão em B
resultado = conjunto_a.issubset(conjunto_b)
print(resultado)  # True

# B ⊆ A → False: B contém 4, 5 e 6 que não existem em A
resultado = conjunto_b.issubset(conjunto_a)
print(resultado)  # False