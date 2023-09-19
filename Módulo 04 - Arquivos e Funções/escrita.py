# write
"Comando para escrever em um arquivo. Se o arquivo não exisitr ele será criado."
"Modo de escrita (w)"

with open(file = 'idades.csv', mode = 'w', encoding = 'utf8') as fp:
  linha = 'idade' + '\n'
  fp.write(linha)
  for idade in idades:
    linha = str(idade) + '\n'
    fp.write(linha)

