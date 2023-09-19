# Motivação
"Para se conectar a uma rede wi-fi, você precisa de duas informações: o nome da rede e a senha de acesso. Quando você vai acessar uma nova rede, você encontra uma lista de redes disponíveis:"

wifi_disponiveis = ["rede1", "cnx_cnx", "uai-fi", "r3d3"]
print(wifi_disponiveis)
"Você consegue identificar quais são os nomes de redes e suas respectivas senhas? Talvez uma list não seja a melhor oção para armazenar esse tipo de dado."

# Definição
"Armazenam sequências no formato chave-valor. São do tipo dict."

brasil = {"capital": "Brasília", "idioma": "Português", "populacao": 210}
print(brasil)
print(type(brasil))

"Não são permitidas chaves duplicadas"

carro = {
  "marca": "Volkswagen",
  "modelo": "Polo",
  "ano": 2021,
  "ano": 2004
}
print(carro)

"Podemos criar dicionários compostos"

cadastro = {
  "tarcisio": {
    "nome": "Tarcísio Almeida",
    "ano_nascimento": 1993,
    "pais": {
      "pai":{
        "nome": "João Tarcísio",
        "ano_nascimento": 1963 
      },
      "mae":{
        "nome": "Maria da Conceição",
        "ano_nascimento": 1963
      },
    }
  }
}
print(cadastro)

cadastro["tarcisio"]["pais"]["mae"]["ano_nascimento"]

# Operações
"Elementos são acessados por sua chave"

credito = {"123": 750, "789": 980}
score_123 = credito["123"]
score_789 = credito["789"]
print(score_123)
print(score_789)

"Elementos são atualizados por sua chave"

credito["123"] = 435
print(credito)

"Para adicionar um novo elemento, basta criar um novo elemento chave-valor"
credito["456"] = 1000
print(credito)

# Métodos
"São métodos nativos do Python que nos ajudam a trabalhar no dia a dia com dicionários"

artigo = dict(
  titulo = "Modulo 02 | Python: Estruturas de Dados",
  corpo = "Topicos, Aulas, Listas, Conjuntos, Dicionários...",
  total_caracteres = 1530
)

# adicionar/ atualizar um elemento pelo chave-valor: dict.update(dict)
print(artigo)
artigo.update({"total_caracteres": 7850})
print(artigo)

# remover um elemento pelo chave: dict.pop(key)
print(artigo)
total_caracteres = artigo.pop("total_caracteres")
print(artigo)

# Conversão
"Podemos converter as chaves e os items de um dicionário em uma lista"

artigo = dict(
  titulo = "Modulo 02 | Python: Estruturas de Dados",
  corpo = "Topicos, Aulas, Listas, Conjuntos, Dicionários...",
  total_caracteres = 1530
)

chaves = list(artigo.keys())
print(chaves)
print(type(chaves))

valores = list(artigo.values())
print(valores)
print(type(valores))

# Revisitando a motivação
"Para se conectar a uma rede wi-fi, você precisa de duas informações: o nome da rede e a senha de acesso. Quando você vai acessar uma nova rede, você encontra uma lista de redes disponíveis:"

wifi_disponiveis = []
rede = {"nome": "rede1", "senha": "cnx_cnx"}
wifi_disponiveis.append(rede)
rede = {"nome": "uai-fi", "senha": "r3d3"}
wifi_disponiveis.append(rede)

print(wifi_disponiveis)
