"""
Arquivo de Estudo: Método .intersection() em Conjuntos
Objetivo: Demonstrar como encontrar os elementos que são comuns
          entre dois ou mais conjuntos utilizando o método .intersection().
"""

# ==============================================================================
# Exemplo 1: Encontrando a Interseção entre Conjuntos com .intersection()
# ------------------------------------------------------------------------------
# O método .intersection() retorna um NOVO conjunto contendo apenas os elementos
# que existem simultaneamente em TODOS os conjuntos comparados.
# Em outras palavras, retorna somente o que os conjuntos têm em comum.
#
# Características importantes:
#   - Não modifica os conjuntos originais (operação não destrutiva).
#   - Equivalente ao operador & (ampersand): conjunto_a & conjunto_b.
#   - Se não houver elementos em comum, retorna um conjunto vazio: set().
#   - Muito utilizado para encontrar dados compartilhados entre coleções,
#     como permissões em comum, produtos favoritos de múltiplos usuários, etc.
# ==============================================================================
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Retorna apenas os elementos que existem nos dois conjuntos: 2 e 3
resultado = conjunto_a.intersection(conjunto_b)
print(resultado)  # {2, 3}