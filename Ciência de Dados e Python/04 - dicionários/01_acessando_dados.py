"""
Arquivo de Estudo: Acesso e Atualização de Dados em Dicionários
Objetivo: Demonstrar como recuperar e modificar valores dentro de um dicionário
          utilizando suas chaves.
"""

# ==============================================================================
# Exemplo 1: Recuperando Valores por Chave
# ------------------------------------------------------------------------------
# Para acessar um valor em um dicionário, informamos a respectiva chave entre
# colchetes []. Diferente de listas e tuplas, aqui não usamos índices numéricos,
# mas as referências (keys) que definimos na criação.
#
# Ponto de atenção: Tentar acessar uma chave que não existe gera um KeyError.
# Para evitar isso, podemos usar o método .get() ou verificar com 'in'.
# ==============================================================================
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])      # "Guilherme"
print(dados["idade"])     # 28
print(dados["telefone"])  # "3333-1234"

# ==============================================================================
# Exemplo 2: Sobrescrevendo Valores
# ------------------------------------------------------------------------------
# Dicionários são objetos mutáveis. Para atualizar o valor de uma chave existente,
# basta atribuir um novo valor ao identificador daquela chave. 
# O valor anterior é descartado e substituído pelo novo.
# ==============================================================================
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}