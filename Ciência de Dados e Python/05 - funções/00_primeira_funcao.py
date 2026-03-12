"""
Arquivo de Estudo: Introdução a Funções em Python
Objetivo: Demonstrar como declarar e chamar funções básicas, trabalhar com 
          parâmetros obrigatórios e parâmetros com valores padrão.
"""

# ==============================================================================
# O que são Funções?
# ------------------------------------------------------------------------------
# Funções são blocos de código reutilizáveis que executam uma tarefa específica.
# Elas ajudam a organizar o código, evitar repetição (DRY - Don't Repeat Yourself)
# e facilitar a manutenção.
# Sintaxe básica: def nome_da_funcao(parametros):
# ==============================================================================

# ==============================================================================
# Exemplo 1: Função Sem Parâmetros
# ------------------------------------------------------------------------------
# Uma função simples que não recebe nenhuma entrada e executa uma ação direta.
# ==============================================================================
def exibir_mensagem():
    print("Olá mundo!")


# ==============================================================================
# Exemplo 2: Função Com Parâmetros Obrigatórios
# ------------------------------------------------------------------------------
# Esta função exige que um valor seja passado para o argumento 'nome' no momento
# da chamada. Se não for passado, o Python retornará um erro.
# ==============================================================================
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


# ==============================================================================
# Exemplo 3: Função Com Valores Padrão (Default)
# ------------------------------------------------------------------------------
# Podemos definir um valor padrão para um parâmetro. Se a função for chamada 
# sem argumentos, ela usará esse valor inicial. Se um argumento for passado, 
# o valor padrão será sobrescrito.
# ==============================================================================
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


# --- Execução das Funções ---

# Chamada simples
exibir_mensagem()

# Chamada passando argumento nomeado (keyword argument)
exibir_mensagem_2(nome="Guilherme")

# Chamada sem argumento (usará o padrão "Anônimo")
exibir_mensagem_3()

# Chamada sobrescrevendo o valor padrão
exibir_mensagem_3(nome="Chappie")