# Exceção
"Exceções são erros que podem acontecert durante a execução do nosso código"

"Exemplo: errp de operações numéricas impossíveis"

preco = 132.85
pessoas = 0

valor_por_pessoa = preco / pessoas

"Exemplo: erro por combinações de tipos diferentes"

nome = "Tarcísio Almeida"
idade = 28

apresentacao = "Fala pessoal, meu nome é " + nome + " e eu tenho " + idade + " anos."

"Exemplo: erro de indexação de estrutura de dados"

anos = [2019, 2020, 2021]
ano_atual = anos[3]

cursos = {
  "python": {
    "nome": "Python para Análise de Dados", "duracao": 2.5
  },
  "sql": {
    "nome": "SQL para Análise de Dados", "duracao": 2
  }
}
curso_atual = cursos["analista"]

# Try/Except
preco = 132.85
pessoas = 0

try:
  valor_por_pessoa = preco / pessoas
  print(valor_por_pessoa)
except ZeroDivisionError:
  print("Número de pessoas inválido. Espera-se um valor maior que 0 e obteve-se um valor igual a " + str(pessoas))

anos = [2019, 2020, 2021]
try:
  ano_atual = anos[3]
  print(ano_atual)
except Exception:
  print("Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e " + str(len(anos) - 1))

try:
  ano_atual = anos[3]
  print(ano_atual)
except Exception as exc:
  print("Descrição da exceção: " + str(exc))
  print("Tipo da exceção: " + str(type(exc)))
  print("Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e " + str(len(anos) - 1))

try:
  ano_atual = anos[3]
  print(ano_atual)
except IndexError:
  print("Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e " + str(len(anos) - 1))
except Exception as exc:
  print(exc)
  print("Erro genérico")

  # Try/Except/Finally

  nome = "Tarcísio Almeida"
  idade = 28

  try:
    apresentacao = "Fala pessoal, meu nome é " + nome + " e eu tenho " + idade + " anos."
    print(apresentacao)
  except TypeError:
    idade = str(idade)
  finally:
    print("Segunda chance")
    apresentacao = "Fala pessoal, meu nome é " + nome + " e eu tenho " + idade + " anos."
    print(apresentacao)