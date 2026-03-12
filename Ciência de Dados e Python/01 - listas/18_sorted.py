"""
Arquivo de Estudo: Função nativa Sorted (sorted) em Listas
Objetivo: Demonstrar como ordenar elementos de um iterável sem modificar a 
          lista original, gerando uma nova lista como resultado.
"""

# ==============================================================================
# Diferença entre .sort() e sorted()
# ------------------------------------------------------------------------------
# Enquanto o '.sort()' é um método de lista que altera a própria lista (inplace),
# a função 'sorted()' é uma função integrada (built-in) que pode ser aplicada 
# a qualquer iterável e SEMPRE retorna uma *nova lista* com os itens ordenados.
#
# Isso preserva a integridade dos dados originais, o que é uma excelente 
# prática em muitos cenários de desenvolvimento.
# ==============================================================================

linguagens = ["python", "js", "c", "java", "csharp"]

print("1. Nova lista ordenada por tamanho (Crescente):")
# Usamos a função sorted() passando a regra 'key' com lambda
nova_lista = sorted(linguagens, key=lambda x: len(x))
print(nova_lista)

print("\n2. Nova lista ordenada por tamanho (Decrescente):")
# Combinamos 'key' com o argumento 'reverse'
nova_lista_reversa = sorted(linguagens, key=lambda x: len(x), reverse=True)
print(nova_lista_reversa)

print("\n3. Verificando que a lista original permanece intacta:")
print(linguagens)
