"""
Arquivo de Estudo: Declaração de Dicionários (Dicts)
Objetivo: Demonstrar as diferentes formas de criar e inicializar dicionários em Python,
          incluindo a sintaxe com chaves {}, o construtor dict() e a adição 
          dinâmica de chaves.
"""

# ==============================================================================
# Sobre Dicionários (Dicts)
# ------------------------------------------------------------------------------
# Dicionários são coleções MUTÁVEIS que armazenam dados no formato chave: valor.
#   - Cada chave deve ser ÚNICA e IMUTÁVEL (como strings, números ou tuplas).
#   - Os valores podem ser de qualquer tipo (incluindo outros dicionários ou listas).
#   - A partir do Python 3.7+, os dicionários preservam a ordem de inserção.
# ==============================================================================

# ==============================================================================
# Exemplo 1: Declarando Dicionário com Chaves {}
# ------------------------------------------------------------------------------
# A forma mais comum de declarar um dicionário é usando chaves {}.
# As chaves e valores são separados por dois pontos (:), e os pares por vírgula.
# ==============================================================================
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

# ==============================================================================
# Exemplo 2: Utilizando o Construtor dict()
# ------------------------------------------------------------------------------
# O construtor dict() permite criar dicionários usando argumentos nomeados.
# Note que nesta sintaxe as chaves não levam aspas durante a declaração.
# ==============================================================================
pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# ==============================================================================
# Exemplo 3: Adicionando/Atualizando Dados Dinamicamente
# ------------------------------------------------------------------------------
# Podemos adicionar novas chaves ou atualizar valores existentes informando a
# chave entre colchetes []. Se a chave não existir, ela será criada.
# ==============================================================================
pessoa["telefone"] = "3333-1234"
print(pessoa)  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}