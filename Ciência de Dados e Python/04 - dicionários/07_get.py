"""
Arquivo de Estudo: Método .get() em Dicionários
Objetivo: Demonstrar como acessar valores de forma segura, evitando exceções 
          do tipo KeyError quando uma chave não existe.
"""

# ==============================================================================
# Exemplo 1: Acesso Seguro com .get()
# ------------------------------------------------------------------------------
# Diferente do acesso via colchetes (dict["chave"]), que lança um erro se a 
# chave não for encontrada, o método .get() retorna um valor padrão (None, 
# por default) caso a chave seja inexistente.
# ==============================================================================
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # Isso lançaria um KeyError se descomentado

# Tenta acessar chave inexistente: retorna None por padrão
resultado = contatos.get("chave")  # None
print(resultado)

# ==============================================================================
# Exemplo 2: Definindo um Valor de Retorno Padrão
# ------------------------------------------------------------------------------
# Podemos passar um segundo argumento ao .get(chave, default). Se a chave não 
# existir, o Python retorna esse valor de fallback em vez de None.
# ==============================================================================
resultado = contatos.get("chave", {})  # Retorna um dicionário vazio {} como fallback
print(resultado)

# Quando a chave existe, o valor real é retornado normalmente
resultado = contatos.get("guilherme@gmail.com", {})
print(resultado)  # {"nome": "Guilherme", "telefone": "3333-2221"}