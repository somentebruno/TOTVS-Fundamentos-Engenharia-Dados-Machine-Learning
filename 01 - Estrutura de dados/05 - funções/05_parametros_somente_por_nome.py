"""
Arquivo de Estudo: Parâmetros Somente por Nome (Keyword-Only)
Objetivo: Demonstrar como restringir a passagem de argumentos para que eles 
          sejam aceitos APENAS por nome (chave=valor), utilizando o asterisco (*).
"""

# ==============================================================================
# O que são Parâmetros Somente por Nome?
# ------------------------------------------------------------------------------
# No Python, ao definirmos os parâmetros de uma função, podemos usar o asterisco `*`.
# Tudo o que estiver APÓS o asterisco DEVE, obrigatoriamente, ser passado por NOME.
# Se o asterisco vier após uma barra `/`, os parâmetros entre eles são flexíveis,
# mas os que vêm após o `*` são estritamente Keyword-Only.
# ==============================================================================

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    """
    Parâmetros antes da / (modelo, ano, placa) -> Somente por posição.
    Parâmetros após o * (marca, motor, combustivel) -> Somente por nome.
    """
    print(modelo, ano, placa, marca, motor, combustivel)


# ==============================================================================
# Exemplo 1: Chamada Correta
# ------------------------------------------------------------------------------
# Cumprimos as duas regras:
# 1. 'Palio', 1999 e 'ABC-1234' passados por POSIÇÃO (antes da /).
# 2. 'marca', 'motor' e 'combustivel' passados por NOME (após o *).
# ==============================================================================
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


# ==============================================================================
# Exemplo 2: Chamada Inválida (Gera Erro)
# ------------------------------------------------------------------------------
# Tentar passar 'marca', 'motor' ou 'combustivel' por posição resultará em um 
# TypeError, pois eles foram definidos como Keyword-Only após o `*`.
# ==============================================================================
# criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")