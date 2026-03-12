# Recebe a entrada do usuário (valor e prioridade)
entrada = input().strip()
valor_str, prioridade = entrada.split()
valor = int(valor_str)

# TODO: Implemente a lógica condicional para decidir entre "aprovado", "revisao" ou "rejeitado" conforme as regras do desafio.

if valor <= 1000 and ((prioridade == "alta") or (prioridade == "media")):
  print("aprovado")
elif valor > 1000 and prioridade == "alta":
  print("revisao")
else: 
  print("rejeitado")