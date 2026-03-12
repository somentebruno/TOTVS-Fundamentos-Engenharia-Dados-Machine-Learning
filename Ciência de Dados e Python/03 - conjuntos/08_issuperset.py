"""
Arquivo de Estudo: Método .issuperset() em Conjuntos
Objetivo: Demonstrar como verificar se um conjunto contém todos os elementos
          de outro conjunto, sendo assim um superconjunto.
"""

# ==============================================================================
# Exemplo 1: Verificando Superconjunto com .issuperset()
# ------------------------------------------------------------------------------
# O método .issuperset() retorna True se o conjunto chamador contiver TODOS os
# elementos do conjunto passado como argumento. É o inverso do .issubset().
#
# Em termos matemáticos: A ⊇ B (A é superconjunto de B)
# significa que todo elemento de B também pertence a A.
#
# Características importantes:
#   - É uma verificação booleana (retorna True ou False).
#   - Equivalente ao operador >=: conjunto_b >= conjunto_a.
#   - Relação inversa ao .issubset(): se A.issubset(B) → True,
#     então B.issuperset(A) → True (e vice-versa).
#   - Um conjunto é sempre superconjunto de si mesmo (A.issuperset(A) → True).
#   - Todo conjunto é superconjunto do conjunto vazio set().
# ==============================================================================
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# A ⊇ B → False: A não contém todos os elementos de B (faltam 4, 5 e 6)
resultado = conjunto_a.issuperset(conjunto_b)
print(resultado)  # False

# B ⊇ A → True: B contém todos os elementos de A (1, 2 e 3)
resultado = conjunto_b.issuperset(conjunto_a)
print(resultado)  # True