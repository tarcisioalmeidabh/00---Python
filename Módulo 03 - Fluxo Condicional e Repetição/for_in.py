# for/in
"Estrutura que permite a execução repetida de um bloco de código repetidas vezes."

"""
for variavel_temporaria in colecao:
<execute este código>  
"""

c = ["a", "b", "c"]
for char in c:
  print(char)

  # for/in/range
  "Estrutura que permite a execução repetida de um bloco de código n vezes."

for valor in range(6):
  print(valor)

soma = 0
for valor in range(0, 10):
  soma = soma + valor
  print(soma)

for multiplo_dois in range(2, 10, 2):
  print(multiplo_dois)


# for/in/list
"Estrutura que permite a execução de um bloco de código para todos os elementos de uma lista."

frutas = ["maca", "banana", "laranja", "uva", "pera"]
for fruta in frutas:
  print(fruta)

frase = "Fala pessoal, meu nome é Tarcísio Almeida"
for caracter in frase:
  if (caracter == "T") | (caracter == "A"):
    print(f'A letra "{caracter}" está presente na frase.')

# for/in/dict
"Estrutura que permite a execução de um bloco de código para todos os elementos de um dicionário."

credito = {"123": 750, "456":812, "789": 980}
for chave, valor in credito.items():
  print(f'Para o documento {chave}, o valor do score de crédito é {credito[chave]}.')
  print('\n')

for chave in credito.keys():
  print(chave)
  print(credito[chave])
  print(f'Para o documento {chave}, o valor do score de crédito é {credito[chave]}.')
  print('\n')

for valor in credito.values():
  print(valor)
  print(f'O valor do score de crédito é {valor}, mas não temos mais as chaves. :(')
  print('\n')

  # break/continue
  "Estrutura que permite a quebra ou o avanço de um laço de repetição."

for i in range(0, 10*10*10*10*10*10):
  print(i)
  if i ==10:
    break

numero = 10
if numero % 2 == 0:
  print(f'O número {numero} é par.')
else:
  print(f'O número {numero} é ímpar.')

  numeros = [361, 553, 194, 13, 510, 33, 135]
  for numero in numeros:
    if numero % 2 ==0:
      print(f'O número {numero} é par.')
      break
    else:
      print(f'O número {numero} é ímpar.')

for numero in numeros:
  if numero % 2 ==0:
    print(f'O número {numero} é par.')
    break
  else:
    continue
    print(f'O número {numero} é ímpar.')