"""
Arquivo de Estudo: Palavra-chave 'del' em Dicionários
Objetivo: Demonstrar como remover itens de um dicionário ou atributos de um 
          dicionário aninhado utilizando a palavra-chave 'del'.
"""

# ==============================================================================
# Sobre o uso de 'del'
# ------------------------------------------------------------------------------
# A palavra-chave 'del' é uma instrução do Python (statement) usada para remover 
# referências de objetos. No contexto de dicionários, ela remove a chave e 
# seu valor associado permanentemente.
#
# Diferente do .pop(), o 'del' não retorna o valor removido. Se tentarmos 
# deletar uma chave que não existe, será lançado um KeyError.
# ==============================================================================
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Removendo um atributo específico de um dicionário aninhado
del contatos["guilherme@gmail.com"]["telefone"]

# Removendo um item completo (chave pai e seu valor/dicionário interno)
del contatos["chappie@gmail.com"]

# O resultado reflete as exclusões:
# 1. Guilherme perdeu a chave "telefone"
# 2. Chappie foi removido inteiramente do dicionário contatos
print(contatos)