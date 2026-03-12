"""
Arquivo de Estudo: Método .update() em Dicionários
Objetivo: Demonstrar como atualizar chaves existentes ou adicionar novos itens
          a um dicionário a partir de outro dicionário ou iterável.
"""

# ==============================================================================
# Exemplo 1: Atualizando itens existentes e adicionando novos com .update()
# ------------------------------------------------------------------------------
# O método .update() permite fundir um novo dicionário (ou qualquer iterável de 
# pares chave-valor) ao dicionário atual. 
#
# Comportamento:
#   1. Chave já existente: O valor é sobrescrito pelo novo valor fornecido.
#   2. Chave inexistente: O par chave-valor é adicionado ao dicionário.
#
# Esta é a forma mais eficiente de realizar múltiplas alterações de uma só vez,
# em vez de fazer várias atribuições manuais.
# ==============================================================================
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Atualizando um registro existente: "Guilherme" vira "Gui"
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

# Adicionando um novo registro que não existia anteriormente
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})

# O dicionário agora contém ambos os registros (um atualizado e um novo)
print(contatos)