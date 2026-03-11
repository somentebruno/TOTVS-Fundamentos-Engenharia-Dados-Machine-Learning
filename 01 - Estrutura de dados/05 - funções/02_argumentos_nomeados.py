"""
Arquivo de Estudo: Argumentos Nomeados em Funções (Keyword Arguments)
Objetivo: Demonstrar como passar argumentos para funções utilizando o nome dos 
          parâmetros, garantindo clareza e flexibilidade, além do uso de 
          desempacotamento de dicionários (**kwargs).
"""

# ==============================================================================
# Argumentos Nomeados
# ------------------------------------------------------------------------------
# Ao chamar uma função, podemos passar os valores informando o nome do parâmetro
# (chave=valor). Isso permite passar os argumentos em qualquer ordem e torna o
# código mais legível e autoexplicativo.
# ==============================================================================

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# --- Formas de Chamada ---

# 1. Chamada Posicional (Lógica padrão, depende da ordem correta)
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# 2. Chamada com Argumentos Nomeados (Keyword Arguments)
# Mais seguro, pois os nomes garantem que o dado correto caia no parâmetro certo.
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# 3. Chamada com Desempacotamento de Dicionário (**kwargs)
# Passamos um dicionário e o Python desempacota as chaves como nomes de argumentos.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})