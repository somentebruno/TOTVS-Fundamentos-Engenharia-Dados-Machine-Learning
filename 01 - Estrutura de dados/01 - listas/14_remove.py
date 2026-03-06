"""
Arquivo de Estudo: Método Remove (.remove) em Listas
Objetivo: Demonstrar como remover a primeira ocorrência de um objeto 
          específico dentro de uma lista utilizando o seu valor.
"""

# ==============================================================================
# Exemplo: Removendo elementos por valor com .remove()
# ------------------------------------------------------------------------------
# Diferente do '.pop()' que remove por índice, o método '.remove()' localiza 
# o primeiro item que corresponde ao valor passado no argumento e o exclui 
# da lista.
#
# Pontos de Atenção:
# 1. Ele remove apenas a PRIMEIRA ocorrência encontrada (da esquerda para a direita).
# 2. Se o valor não existir na lista, o Python lançará um erro (ValueError).
# ==============================================================================

linguagens = ["python", "js", "c", "java", "csharp"]

print("Lista antes da remocao de 'c':")
print(linguagens)

# Removendo o objeto 'c' através do seu valor direto
linguagens.remove("c")

print("\nLista apos a remocao:")
print(linguagens)  # ["python", "js", "java", "csharp"]