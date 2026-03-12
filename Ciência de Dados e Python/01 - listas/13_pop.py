"""
Arquivo de Estudo: Método Pop (.pop) em Listas
Objetivo: Demonstrar como remover e retornar o último elemento de uma lista 
          (comportamento de pilha) ou um elemento em um índice específico.
"""

# ==============================================================================
# Exemplo: Removendo elementos com .pop()
# ------------------------------------------------------------------------------
# O método '.pop()' remove um item da lista e, ao mesmo tempo, retorna esse 
# item para que possa ser armazenado em uma variável ou exibido.
#
# Comportamentos:
# 1. Sem argumentos: Remove e retorna o ÚLTIMO elemento (LIFO - Last In, First Out).
# 2. Com argumento (índice): Remove e retorna o elemento daquela posição específica.
#
# É uma ferramenta essencial para implementar estruturas de dados como pilhas.
# ==============================================================================

linguagens = ["python", "js", "c", "java", "csharp"]

print("Removendo o último (padrão):")
print(linguagens.pop())  # csharp

print("\nRemovendo o próximo último:")
print(linguagens.pop())  # java

print("\nRemovendo mais um:")
print(linguagens.pop())  # c

print("\nRemovendo o elemento no índice 0 (primeiro):")
print(linguagens.pop(0))  # python