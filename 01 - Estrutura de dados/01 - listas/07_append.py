"""
Arquivo de Estudo: Método Append (.) em Listas
Objetivo: Demonstrar como adicionar elementos de diferentes tipos de dados 
          ao final de uma lista existente.
"""

# ==============================================================================
# Exemplo: Adicionando dados dinamicamente com .append()
# ------------------------------------------------------------------------------
# Diferente de linguagens estaticamente tipadas, as listas em Python são 
# extremamente flexíveis e podem armazenar múltiplos tipos de objetos 
# (inteiros, strings e até mesmo outras listas) simultaneamente em uma única 
# estrutura, bastando apenas anexá-los usando o método '.append()'. 
#
# O método '.append()' SEMPRE insere o novo elemento na última posição 
# (final) da lista original, evitando a necessidade de controle de tamanho.
# ==============================================================================

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]