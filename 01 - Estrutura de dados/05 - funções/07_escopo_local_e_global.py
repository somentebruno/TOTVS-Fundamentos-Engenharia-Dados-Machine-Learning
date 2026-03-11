"""
Arquivo de Estudo: Escopo Local e Global em Python
Objetivo: Demonstrar como o Python lida com variáveis dentro e fora de funções,
          e como utilizar a palavra reservada 'global' para modificar variáveis
          do escopo externo.
"""

# ==============================================================================
# Escopo Local vs Global
# ------------------------------------------------------------------------------
# Escopo Global: Variáveis declaradas fora de funções, visíveis em todo o arquivo.
# Escopo Local: Variáveis declaradas dentro de uma função, visíveis apenas ali.
# Palavra 'global': Informa que a função deve usar/alterar a variável global, 
#                  em vez de criar uma local com o mesmo nome.
# ==============================================================================

salario = 2000


def salario_bonus(bonus):
    """
    Indica ao Python que queremos manipular a variável 'salario' que está no 
    escopo global. Sem o 'global salario', o Python tentaria criar uma nova
    variável local, o que geraria um erro de cálculo (UnboundLocalError).
    """
    global salario
    salario += bonus
    return salario


# ==============================================================================
# Exemplo de Execução
# ------------------------------------------------------------------------------
# Ao chamarmos a função, o valor da variável global 'salario' é alterado.
# ==============================================================================
print(f"Salário inicial: {salario}")
final = salario_bonus(500)  
print(f"Salário após bônus: {final}") # Saída esperada: 2500