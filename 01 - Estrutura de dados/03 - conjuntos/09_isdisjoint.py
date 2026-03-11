"""
Arquivo de Estudo: Método .isdisjoint() em Conjuntos
Objetivo: Demonstrar como verificar se dois conjuntos são disjuntos,
          ou seja, se não possuem nenhum elemento em comum.
"""

# ==============================================================================
# Exemplo 1: Verificando Conjuntos Disjuntos com .isdisjoint()
# ------------------------------------------------------------------------------
# O método .isdisjoint() retorna True se os dois conjuntos não compartilharem
# NENHUM elemento em comum. Caso haja ao menos um elemento em comum,
# retorna False.
#
# Em termos matemáticos: A ∩ B = ∅ (a interseção entre A e B é vazia)
# significa que A e B são conjuntos disjuntos.
#
# Características importantes:
#   - É uma verificação booleana (retorna True ou False).
#   - É comutativo: A.isdisjoint(B) == B.isdisjoint(A).
#   - Útil para validar ausência de conflitos entre coleções de dados,
#     como permissões, categorias, tags exclusivas, etc.
#   - Dois conjuntos vazios são sempre disjuntos entre si.
# ==============================================================================
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# A ∩ B = ∅ → True: A e B não têm nenhum elemento em comum
resultado = conjunto_a.isdisjoint(conjunto_b)
print(resultado)  # True

# A ∩ C ≠ ∅ → False: A e C compartilham o elemento 1
resultado = conjunto_a.isdisjoint(conjunto_c)
print(resultado)  # False