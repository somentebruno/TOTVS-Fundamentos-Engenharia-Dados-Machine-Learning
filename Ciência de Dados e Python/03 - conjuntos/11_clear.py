"""
Arquivo de Estudo: Método .clear() em Conjuntos
Objetivo: Demonstrar como remover todos os elementos de um conjunto de uma vez,
          deixando-o vazio sem destruir a referência ao objeto.
"""

# ==============================================================================
# Exemplo 1: Esvaziando um Conjunto com .clear()
# ------------------------------------------------------------------------------
# O método .clear() remove TODOS os elementos do conjunto, deixando-o vazio.
# A diferença crucial entre .clear() e deletar a variável (del sorteio) é:
#   - .clear() mantém o objeto conjunto na memória, apenas o esvazia.
#   - del sorteio remove a referência completamente da memória.
#
# Características importantes:
#   - Modifica o conjunto original diretamente (operação in-place).
#   - Não retorna nada (retorna None).
#   - Após o .clear(), o conjunto resulta em set() (conjunto vazio).
#   - Atenção: {} cria um dicionário vazio, não um conjunto vazio!
#     Para criar um conjunto vazio, use sempre set().
# ==============================================================================
sorteio = {1, 23}

print(sorteio)  # {1, 23}

# Remove todos os elementos do conjunto, mantendo a variável em memória
sorteio.clear()

print(sorteio)  # set()