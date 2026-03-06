"""
Arquivo de Estudo: Método Sort (.sort) em Listas
Objetivo: Demonstrar as diversas formas de ordenação de listas, incluindo 
          ordenação padrão, inversa e personalizada por critérios.
"""

# ==============================================================================
# Conceito de Ordenação Direta (.sort)
# ------------------------------------------------------------------------------
# O método '.sort()' organiza os elementos da lista original (inplace).
# Por padrão, a ordenação é feita de forma ascendente (alfabética ou numérica).
# ==============================================================================

linguagens = ["python", "js", "c", "java", "csharp"]

# 1. Ordenação Alfabética Padrão
linguagens.sort()
print("1. Ordem Alfabetica:")
print(linguagens)  # ["c", "csharp", "java", "js", "python"]

# 2. Ordenação Espelhada (Inversa)
# O argumento 'reverse=True' inverte a lógica da ordenação.
linguagens.sort(reverse=True)
print("\n2. Ordem Alfabetica Inversa:")
print(linguagens)  # ["python", "js", "java", "csharp", "c"]

# 3. Ordenação por Critério Personalizado (Key)
# O argumento 'key' aceita uma função (ex: lambda) que define a regra de ordenação.
# Abaixo, ordenamos pelo tamanho da string (len).
linguagens.sort(key=lambda x: len(x))
print("\n3. Ordenado por Tamanho (Crescente):")
print(linguagens)  # ["c", "js", "java", "python", "csharp"]

# 4. Ordenação por Tamanho de forma Inversa
linguagens.sort(key=lambda x: len(x), reverse=True)
print("\n4. Ordenado por Tamanho (Decrescente):")
print(linguagens)  # ["python", "csharp", "java", "js", "c"]