# Lê a linha de entrada e separa os valores
print(f"Digite o valor do produto e o percentual de desconto na mesma linha: ")
entrada = input().strip().split()

valor_total = float(entrada[0])

percentual_desconto = int(entrada[1])



#TODO: Calcule o valor final do pedido após aplicar o desconto percentual

valor_do_desconto = valor_total * (percentual_desconto / 100)
valor_final = valor_total - valor_do_desconto


# Imprima o valor final com duas casas decimais

print(f"O valor final com desconto é: {valor_final:.2f}")