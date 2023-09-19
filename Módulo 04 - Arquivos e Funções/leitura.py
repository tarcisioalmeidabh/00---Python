# Criando um arquivo csv de exemplo.
import readline

%%writefile banco.csv
age,job,marital,education,default,balance,housing,loan
30,unemployed,married,primary,no,1787,no,no
33,services,married,secondary,no,4789,yes,yes
35,management,single,tertiary,no,1350,yes,no
30,management,married,tertiary,no,1476,yes,yes
59,blue-collar,married,secondary,no,0,yes,no
35,management,single,tertiary,no,747,no,no
36,self-employed,married,tertiary,no,307,yes,no
39,technician,married,secondary,no,147,yes,no
41,entrepreneur,married,tertiary,no,221,yes,no
43,services,married,primary,no,-88,yes,yes

# with/open
"Comando para ler arquivos"
"""
with open(file = '<caminho do arquivo', mode = '<modo de leitura>', encoding = '<decodificador>') as <apelido>:
  bloco de código
"""

"""Os modos de leitura são:
r: Abrir o arquivo para leitura (padrão)
w: Abrir o arquivo para escrita (sobrescreve o arquivo original)
a: Abrir o arquivo para acrescentar (não sobrescreve o arquivo original)
"""

# read
"Comando par ler todo o conteúdo de um arquivo."
conteudo = None
with open(file='./banco.csv', mode = 'r', encoding = 'utf8') as arquivo:
  conteudo = arquivo.read()
  print(conteudo)

  #readline
  "Comando para ler o conteúdo de um arquivo uma linha por vez."

  conteudo = []
  with open(file = './banco.csv', mode = 'r', encoding = 'utf8') as arquivo:
    linha = arquivo.readline() #lê a primeira linha
    while linha:
      conteudo.append(linha)
      linha = arquivo.readline() #lê uma nova inha, se a linha não existir, salva o valor None.
      print(conteudo)

for linha in conteudo:
  print(linha)

# Exemplo: Extraindo os valores da primeira coluna (idade).

idades = []
with open(file = './banco.csv', mode = 'r', encoding = 'utf8') as arquivo:
  linha = arquivo.readline() #lê o cabeçalho
  linha = arquivo.readline() #lê a primeira linha
  while linha:
    linha_separada = linha.split(sep=',') #quebra a string nas vírgulas e salva os resultados em uma lista
    idade = linha_separada[0] #seleciona o primeiro elemento da lista
    #idade = int(idade) #converte o valor de string para integer
    idades.append(idade) #salva o valor na lista de idades
    linha = arquivo.readline() #lê uma nova linha, se a linha não existir, salva o valor None.
    print(idades)

    # write
"Comando para escrever em um arquivo. Se o arquivo não exisitr ele será criado."
"Modo de escrita (w)"

with open(file = 'idades.csv', mode = 'w', encoding = 'utf8') as fp:
  linha = 'idade' + '\n'
  fp.write(linha)
  for idade in idades:
    linha = str(idade) + '\n'
    fp.write(linha)

"Modo de acréscimo (w)"

with open(file = 'idades.csv', mode = 'a', encoding = 'utf8') as fp:
  for idade in idades:
    linha = str(idade + 100) + '\n'
    fp.write(linha)