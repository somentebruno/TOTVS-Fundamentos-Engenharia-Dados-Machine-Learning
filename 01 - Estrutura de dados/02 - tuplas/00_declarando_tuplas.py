"""
Arquivo de Estudo: Declaração de Tuplas
Objetivo: Demonstrar as diferentes formas de criar e inicializar tuplas em Python,
          incluindo a sintaxe com parênteses, uso do construtor tuple() e a 
          peculiaridade da tupla com um único elemento.
"""

# ==============================================================================
# Exemplo 1: Declarando Tupla com Parênteses
# ------------------------------------------------------------------------------
# As tuplas são estruturas de dados imutáveis (seus elementos não podem ser 
# alterados depois de criadas). A forma mais comum de declarar uma tupla é 
# colocando os elementos dentro de parênteses e separados por vírgula.
# É comum colocar a vírgula após o último elemento quando a declaração
# é feita em múltiplas linhas.
# ==============================================================================
frutas = (
    "laranja",
    "uva",
    "banana",
    "maçã",
)

print(frutas)

# ==============================================================================
# Exemplo 2: Utilizando o Construtor tuple() com Strings
# ------------------------------------------------------------------------------
# O construtor built-in tuple() pode receber qualquer iterável como argumento e 
# convertê-lo em uma tupla. Ao passarmos uma string, cada caractere se torna
# um elemento independente dentro da tupla resultante.
# ==============================================================================
letras = tuple("python")
print(letras)

# ==============================================================================
# Exemplo 3: Convertendo Listas para Tuplas
# ------------------------------------------------------------------------------
# Podemos passar uma lista para o construtor tuple(), convertendo-a em tupla.
# É útil quando precisamos "congelar" dados de uma lista para impedir
# modificações futuras.
# ==============================================================================
numeros = tuple([1, 2, 3, 4])
print(numeros)

# ==============================================================================
# Exemplo 4: Declarando Tupla de um Único Elemento (Singleton)
# ------------------------------------------------------------------------------
# Ponto crítico: a criação de uma tupla com apenas um elemento exige uma vírgula
# ao final ("Brasil",). Se a vírgula for omitida ("Brasil"), o Python ignorará
# os parênteses e considerará apenas o tipo primitivo (no caso, string).
# A vírgula é o que realmente define a estrutura de tupla.
# ==============================================================================
pais = ("Brasil",)
print(pais)