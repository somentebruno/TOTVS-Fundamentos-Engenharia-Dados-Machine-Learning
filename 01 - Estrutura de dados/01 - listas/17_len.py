"""
Arquivo de Estudo: Função nativa Len (len) em Listas
Objetivo: Demonstrar como obter a quantidade total de elementos de um objeto 
          iterável (neste caso, uma lista).
"""

# ==============================================================================
# Exemplo: Verificando o tamanho da lista com len()
# ------------------------------------------------------------------------------
# A função 'len()' é uma das funções integradas (built-ins) mais utilizadas do Python.
# Ela retorna um número inteiro que representa o comprimento (length) da lista.
#
# É fundamental para controles de laços (loops), validações de dados e 
# lógica de negócios onde o volume de itens impacta o processamento.
# ==============================================================================

linguagens = ["python", "js", "c", "java", "csharp"]

# Obtendo e exibindo o tamanho total da lista
tamanho = len(linguagens)

print(f"Lista de linguagens: {linguagens}")
print(f"A lista possui {tamanho} elementos.")