"""
Arquivo de Estudo: Método .add() em Conjuntos
Objetivo: Demonstrar como adicionar novos elementos a um conjunto
          e como a unicidade é mantida automaticamente ao inserir duplicatas.
"""

# ==============================================================================
# Exemplo 1: Adicionando Elementos com .add()
# ------------------------------------------------------------------------------
# O método .add(elemento) insere um único elemento no conjunto.
# A principal característica é que, se o elemento já existir, ele é
# simplesmente ignorado — sem erros e sem duplicatas.
#
# Características importantes:
#   - Modifica o conjunto original diretamente (operação in-place).
#   - Não retorna nada (retorna None).
#   - Diferente de listas, não há .append() em sets — o método é .add().
#   - Para adicionar múltiplos elementos de uma vez, use .update() no lugar.
#   - Aceita apenas elementos imutáveis (strings, números, tuplas).
#     Tentar adicionar uma lista causa TypeError.
# ==============================================================================
sorteio = {1, 23}

# Adiciona o número 25 ao conjunto
sorteio.add(25)
print(sorteio)  # {1, 23, 25}

# Adiciona o número 42 ao conjunto
sorteio.add(42)
print(sorteio)  # {1, 23, 25, 42}

# Tenta adicionar 25 novamente → ignorado, conjunto permanece inalterado
sorteio.add(25)
print(sorteio)  # {1, 23, 25, 42}