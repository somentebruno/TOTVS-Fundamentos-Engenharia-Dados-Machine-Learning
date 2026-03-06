"""
Arquivo de Estudo: Método Clear (.clear) em Listas
Objetivo: Demonstrar como limpar/esvaziar completamente uma lista existente.
"""

# ==============================================================================
# Exemplo: Esvaziando a lista com .clear()
# ------------------------------------------------------------------------------
# O método '.clear()' é uma função inplace que remove *todos* os itens 
# da lista de uma única vez, liberando os dados armazenados mas mantendo o
# objeto da lista na memória da aplicação, resultando em uma lista vazia: [].
#
# Diferença importante: O uso de '.clear()' é diferente de deletar a lista 
# inteira da memória com `del lista`. Ele apenas reseta o estado interno 
# dos dados (tamanho 0).
# ==============================================================================

lista = [1, "Python", [40, 30, 20]]

print("Antes do clear:")
print(lista)  # [1, "Python", [40, 30, 20]]

lista.clear()

print("\nDepois do clear:")
print(lista)  # []