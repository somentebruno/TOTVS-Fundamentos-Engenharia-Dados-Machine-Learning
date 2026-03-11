"""
Arquivo de Estudo: Método .keys() em Dicionários
Objetivo: Demonstrar como obter uma visão de todas as chaves presentes em um 
          dicionário.
"""

# ==============================================================================
# Exemplo 1: Obtendo as Chaves com .keys()
# ------------------------------------------------------------------------------
# O método .keys() retorna um objeto do tipo 'dict_keys', que é uma visão 
# dinâmica de todas as chaves contidas no dicionário. 
# 
# Esta função é útil quando precisamos verificar quais identificadores estão 
# disponíveis ou quando queremos realizar operações apenas sobre os nomes 
# dos atributos (chaves) sem carregar os valores em memória.
# ==============================================================================
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Retorna uma visão contendo apenas as chaves do dicionário
resultado = contatos.keys()
print(resultado)  # dict_keys(['guilherme@gmail.com'])