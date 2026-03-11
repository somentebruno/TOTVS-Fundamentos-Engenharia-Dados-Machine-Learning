"""
Arquivo de Estudo: Método .setdefault() em Dicionários
Objetivo: Demonstrar como garantir que uma chave exista em um dicionário,
          atribuindo um valor padrão apenas se a chave não estiver presente.
"""

# ==============================================================================
# Exemplo 1: Garantindo chaves com .setdefault()
# ------------------------------------------------------------------------------
# O método .setdefault(chave, valor_padrao) funciona da seguinte forma:
#   1. Se a CHAVE JÁ EXISTE: ele retorna o valor atual e NÃO altera o dicionário.
#   2. Se a CHAVE NÃO EXISTE: ele adiciona a chave com o valor_padrao informado 
#      e retorna esse novo valor.
#
# É uma forma muito eficiente de inicializar valores sem precisar de um if 
# para verificar se a chave existe antes de atribuir.
# ==============================================================================
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# Tenta definir "nome", mas ela já existe -> Retorna "Guilherme" e não altera nada
contato.setdefault("nome", "Giovanna") 
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# Tenta definir "idade", que NÃO existe -> Adiciona a chave com o valor 28
contato.setdefault("idade", 28) 
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}