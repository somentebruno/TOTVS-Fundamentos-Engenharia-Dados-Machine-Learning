"""
Arquivo de Estudo: Método .copy() em Conjuntos
Objetivo: Demonstrar como criar uma cópia independente (shallow copy) de um
          conjunto, evitando que alterações em um afete o outro.
"""

# ==============================================================================
# Exemplo 1: Copiando um Conjunto com .copy()
# ------------------------------------------------------------------------------
# O método .copy() retorna uma NOVA cópia rasa (shallow copy) do conjunto.
# O conjunto original permanece intacto.
#
# A importância do .copy() fica clara ao comparar com a atribuição simples:
#   copia = sorteio      → ambas as variáveis apontam para o MESMO objeto.
#                          Alterar uma altera a outra!
#   copia = sorteio.copy() → cria um objeto NOVO e independente.
#                          Alterações em uma não afetam a outra.
#
# Características importantes:
#   - O conjunto original não é modificado (operação não destrutiva).
#   - Retorna um novo objeto set com os mesmos elementos.
#   - É uma cópia rasa: elementos internos imutáveis são compartilhados,
#     mas a estrutura do conjunto em si é independente.
# ==============================================================================
sorteio = {1, 23}

print(sorteio)  # {1, 23}

# Cria uma cópia independente do conjunto original
copia = sorteio.copy()

print(copia)    # {1, 23} — novo objeto, mesmos valores