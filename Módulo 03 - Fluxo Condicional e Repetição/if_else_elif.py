# IF/ELSE
"Estrutura de alteração de fluxo lógico do código, avalia um valor booleano ou uma comparação lógica. Note a identação do código"

"""
if <booleano / comparação lógica == True:
  <execute este código>
else:
  <senão execute este código>
  """

if True:
  print("Verdadeiro")
else:
  print("Falso")

# Exemplo: Código de segurança de um cartão de crédito

codigo_de_seguranca = "827"
codigo_de_seguranca_cadastro = "010"
pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

if pode_efetuar_pagamento:
  print("Pagamento efetuado")
else:
  print("Erro: Código de segurança inválido")

codigo_de_seguranca = "827"
codigo_de_seguranca_cadastro = "010"
senha = "7783"
senha_cadastro = "7783"

if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
  print("Pagamento efetuado")
else:
  print("Erro: pagamento não efetuado")

if (codigo_de_seguranca != codigo_de_seguranca_cadastro) | (senha != senha_cadastro):
  print("Erro: pagamento não efetuado")
else:
  print("Pagamento efetuado")

# IF/ELIF/ELSE
"Podemos também avaliar múltiplas condições"

"""
if <1º booleano / 1ª comparação lógica == True:
  <execute este código se a primeira condição for verdade>
elif <2º booleano / 2ª comparação lógica == True:
  <execute este código se a segunda condição for verdade>
else:
  <senão execute este código>
  """
codigo_de_seguranca = "827"
codigo_de_seguranca_cadastro = "010"
senha = "7783"
senha_cadastro = "7783"

if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
  print("Pagamento efetuado")
elif (codigo_de_seguranca != codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
  print("Erro: pagamento não efetuado")
elif (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha != senha_cadastro):
  print("Erro: pagamento não efetuado")
else:
  print("Erro: pagamento não efetuado")
