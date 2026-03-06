"""
Arquivo de Estudo: Método Index (.index) em Listas
Objetivo: Demonstrar como localizar a primeira ocorrência de um objeto 
          dentro de uma lista e retornar seu índice.
"""

# ==============================================================================
# Exemplo: Localizando índices com .index()
# ------------------------------------------------------------------------------
# O método '.index()' procura pelo elemento especificado e retorna a posição 
# (índice) da sua primeira aparição. 
#
# Importante: Caso o item não exista na lista, o Python lançará um erro 
# (ValueError). Por isso, em aplicações reais, é comum verificar se o item 
# existe antes de chamar o '.index()' ou tratar a exceção.
# ==============================================================================

linguagens = ["python", "js", "c", "java", "csharp"]

print("Índice da primeira ocorrência de 'java':")
print(linguagens.index("java"))  # 3

print("\nÍndice da primeira ocorrência de 'python':")
print(linguagens.index("python"))  # 0
# Exemplo de erro: Se tentarmos buscar algo que não existe, o Python lança um erro.
# Descomente a linha abaixo para ver o ValueError em ação:
# print(linguagens.index("ruby"))