"""
Arquivo de Estudo: Método .values() em Dicionários
Objetivo: Demonstrar como obter uma visão de todos os valores presentes em um 
          dicionário, ignorando as chaves.
"""

# ==============================================================================
# Exemplo 1: Obtendo todos os valores com .values()
# ------------------------------------------------------------------------------
# O método .values() retorna um objeto do tipo 'dict_values', que é uma visão 
# dinâmica de todos os VALORES contidos no dicionário. 
#
# Características:
#   - Diferente do .keys() ou .items(), ele não traz os identificadores (chaves).
#   - É muito útil quando precisamos realizar operações estatísticas, buscas 
#     ou processamentos que dependem apenas dos dados armazenados e não 
#     de como eles estão indexados.
#   - Retorna os valores na ordem correspondente às suas chaves.
# ==============================================================================
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Retorna uma visão contendo apenas os valores (os dicionários internos)
resultado = contatos.values()

print(resultado) 
# dict_values([
#     {'nome': 'Guilherme', 'telefone': '3333-2221'}, 
#     {'nome': 'Giovanna', 'telefone': '3443-2121'}, 
#     {'nome': 'Chappie', 'telefone': '3344-9871'}, 
#     {'nome': 'Melaine', 'telefone': '3333-7766'}
# ])