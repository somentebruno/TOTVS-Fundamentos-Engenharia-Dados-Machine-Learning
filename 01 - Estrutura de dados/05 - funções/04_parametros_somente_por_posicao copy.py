"""
Arquivo de Estudo: Parâmetros Somente por Posição (Positional-Only)
Objetivo: Demonstrar como restringir a passagem de certos argumentos para que eles 
          sejam aceitos APENAS por posição, utilizando a barra diagonal (/).
"""

# ==============================================================================
# O que são Parâmetros Somente por Posição?
# ------------------------------------------------------------------------------
# No Python, ao definirmos os parâmetros de uma função, podemos usar a barra `/`.
# Tudo o que estiver ANTES da barra DEVE, obrigatoriamente, ser passado por POSIÇÃO.
# Não é permitido o uso de nomes de parâmetros para esses argumentos. Após a 
# barra, os parâmetros podem ser posicionais ou nomeados.
# ==============================================================================

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    """
    Parâmetros antes da / (modelo, ano, placa) -> Somente por posição.
    Parâmetros após a / (marca, motor, combustivel) -> Podem ser posição ou nomeados.
    """
    print(modelo, ano, placa, marca, motor, combustivel)


# ==============================================================================
# Exemplo 1: Chamada Correta (Mista)
# ------------------------------------------------------------------------------
# Passamos os três primeiros argumentos pela ordem em que foram declarados, 
# cumprindo a regra da barra (/). Os seguintes são passados como desejar.
# ==============================================================================
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


# ==============================================================================
# Exemplo 2: Chamada Inválida (Gera Erro)
# ------------------------------------------------------------------------------
# Se tentarmos nomear um parâmetro que está antes da barra, o Python lançará um 
# TypeError informando que a função não aceita argumentos nomeados para 
# aquele parâmetro específico.
# ==============================================================================
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
