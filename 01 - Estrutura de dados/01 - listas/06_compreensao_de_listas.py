"""
Arquivo de Estudo: Compreensão de Listas (List Comprehension)
Objetivo: Demonstrar a criação e manipulação otimizada de listas usando a sintaxe de compreensão de listas, 
          um dos recursos mais poderosos e 'pytônicos' da linguagem.
"""

# ==============================================================================
# Exemplo 1: Filtrando valores de uma lista
# ------------------------------------------------------------------------------
# List Comprehension oferece uma maneira concisa de criar listas com base 
# em listas existentes. A estrutura base é: 
# [expressão for item in iterável if condição]
#
# Isso substitui os blocos 'for' com 'if' aninhados, tornando o código
# mais legível e com execução ligeiramente mais rápida (otimização em C por baixo dos panos).
# ==============================================================================
print("1. Filtrando números pares:")
numeros = [1, 30, 21, 2, 9, 65, 34]

# Condição % 2 == 0 garante que apenas números pares sejam adicionados à nova lista.
pares = [numero for numero in numeros if numero % 2 == 0]
print(f"Lista original: {numeros}")
print(f"Pares filtrados: {pares}")

print("\n" + "-" * 40 + "\n")

# ==============================================================================
# Exemplo 2: Modificando (Mapeando) valores de uma lista
# ------------------------------------------------------------------------------
# Além de filtrar, podemos aplicar uma transformação/operação a cada elemento
# que passa pela iteração (semelhante ao map()).
# A estrutura base sem filtro é: [expressão for item in iterável]
# ==============================================================================
print("2. Elevando valores ao quadrado:")
# Reutilizamos a lista base
numeros = [1, 30, 21, 2, 9, 65, 34]

# Cada numero da lista é multiplicado por ele mesmo (**2).
quadrados = [numero**2 for numero in numeros]
print(f"Lista original: {numeros}")
print(f"Valores ao quadrado: {quadrados}")
print("\n" + "-" * 40 + "\n")