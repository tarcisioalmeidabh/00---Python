#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, world!")


# # Variáveis

# In[4]:


idade = 28
print(idade)

nome = "Tarcísio"
print(nome)


# # Tipos Nativos

# In[6]:


# a definição do nome da variável deve ser representativo ao que estamos tratando

# Tipos Numéricos: inteiro (int) e decimal (float)
preco = 1000
tipo_preco = type(preco)

print(preco)
print(tipo_preco)

juros = 0.05
tipo_juros = type(juros)

print(juros)
print(tipo_juros)


# In[7]:


# Tipos de texto: String (str)

primeiro_nome = "Tarcísio"
print(primeiro_nome)
print(type(primeiro_nome))

pais = "Brasil"
print(pais)
print(type(pais))


# In[9]:


# Por padrão, é recomendado definir o nome da variável como se fosse uma pergunta.
# Tipos Lógicos: Booleanos (bool)

usuario_maior_de_idade = False
print(usuario_maior_de_idade)
print(type(usuario_maior_de_idade))


# In[10]:


# Tipo vazio: NoneType

telefone_fixo = None
print(telefone_fixo)
print(type(telefone_fixo))


# # Motivação

# In[15]:


"""
Você precisa calcular o ticket médio diário (tkt) do seu restaurante.
A métrica é calculada pela soma do valor das vendas (svv) de um mesmo dia
dividido pela quantidade de vendas (sqv), também de um mesmo dia.

tkt = svv/sqv

 Dia       Valor Total Vendas        Qtd Total Vendas     Ticket Médio
19/01           153.98                      3                  ?
20/01           337.01                      7                  ?
23/01           295.33                      5                  ?
"""
print("Como podemos fazer este cálculo usando o Python?")


# # Definição

# In[16]:


# Armazenam valores numéricos:
# 10, 37, 500 (inteiros)
# 0.333, 10.1 (decimais)
# 1, 2j (complexos)

print(type(37))
print(type(10.1))
print(type(1 + 2j))


# # Operações

# In[17]:


# + (soma)
# - (subtração)
# * (multiplicação)
# / (divisão)
# // (divisão inteira)
# ** (potência)
# % (resto de divisão)


#Exemplo: Carrinho de compra de um e-commerce
qtd_itens_carrinho_compra = 0
qtd_itens_carrinho_compra = qtd_itens_carrinho_compra + 1
print(qtd_itens_carrinho_compra)

qtd_itens_carrinho_compra = qtd_itens_carrinho_compra + 1
print(qtd_itens_carrinho_compra)


# In[18]:


qtd_itens_carrinho_compra = 0

qtd_itens_carrinho_compra += 1
print(qtd_itens_carrinho_compra)

qtd_itens_carrinho_compra += 1
print(qtd_itens_carrinho_compra)


# In[19]:


# Exemplo: Total a pagar de um produto

preco = 47
quantidade = 0.250

total_a_pagar = quantidade * preco
print(total_a_pagar)


# In[20]:


a = 3
b = 2

c = a / b
print(c)
print(type(c))

d = a // b
print(d)
print(type(d))


# # Conversão

# In[21]:


print(int(3.9))


# In[22]:


print(float(10))


# In[23]:


print(complex(1))


# # Revisitando a motivação

# In[24]:


"""
Você precisa calcular o ticket médio diário (tkt) do seu restaurante.
A métrica é calculada pela soma do valor das vendas (svv) de um mesmo dia
dividido pela quantidade de vendas (sqv), também de um mesmo dia.

tkt = svv/sqv

 Dia       Valor Total Vendas        Qtd Total Vendas     Ticket Médio
19/01           153.98                      3                  ?
20/01           337.01                      7                  ?
23/01           295.33                      5                  ?
"""


# In[28]:


# Ticket médio diário do dia 19/01.

svv = 153.98
sqv = 3

tkt_19 = svv / sqv
print(tkt)


# In[29]:


# Ticket médio diário do dia 20/01.

svv = 337.01
sqv = 7

tkt_20 = svv / sqv
print(tkt)


# In[30]:


# Ticket médio diário do dia 23/01.

svv = 295.33
sqv = 5

tkt_23 = svv / sqv
print(tkt)


# In[31]:


# Ticket médio

tkt = (tkt_19 + tkt_20 + tkt_23) / 3
print(tkt)


# # Strings

# In[25]:


# Motivação
"""
A empresa que você trabalha adquiriu uma startup de logística. Você precisa identificar todos endereços 
que são comuns a ambas. Na sua empresa, você armazena a latitude e longitude dos endereços em duas 
variáveis lat e lon, já a startup adquirida em uma unica variavel latlon.
"""

# sua empresa
lat = "-22.005320"
lon = "-47.891040"

# startup adquirida
latlon = "-22.005320;-47.891040"


# In[4]:


# Tipo de dados: String (str)

nome_aula = "Aula 04, Módulo 01, Strings"
print(nome_aula)
print(type(nome_aula))


# In[5]:


string_vazia = ""
print(string_vazia)
print(type(string_vazia))


# In[6]:


# Operações

# Exemplo: Nome completo

nome = "Tarcísio"
sobrenome = "Almeida"

apresentacao = "Olá, meu nome é " + nome + " " + sobrenome + "."
print(apresentacao)


# In[10]:


# Exemplo: Nome completo
# Outra forma de fazer é incluindo a letra f antes do texto e chamar as variáveis entre chaves.

nome = "Tarcísio"
sobrenome = "Almeida"

apresentacao = f"Olá, meu nome é {nome} {sobrenome}."
print(apresentacao)


# In[15]:


# Fatiamento

# Exemplo: Informações de e-mail

email = "tarcisioalmeidabh@outlook.com"
print("0: " + email[0])
print("13: " + email[13])
print("-1: " + email[-1])
print("-4: " + email[-4])


# In[13]:


# Fatiamento por intervalo

email_usuario = email[0:8]
print(email_usuario)


# In[16]:


# Métodos

endereco = "Avenida Professor Clóvis Salgado, 747 bloco 01 apto 504 - Bandeirantes (Pampulha), Belo Horizonte/MG"


# In[17]:


# maiusculo: string.upper()

print(endereco.upper())


# In[18]:


# posição: string.find(substring)

posicao = endereco.find("Pampulha")
print(posicao)


# In[19]:


# substituição: string.replace(antigo, novo)

print(endereco.replace("Avenida", "Av."))


# # Conversão

# In[20]:


idade = 28
print(type(idade))
      
idade = str(idade)
print(type(idade))


# In[21]:


faturamento = "R$ 35 mi"
print(faturamento)
print(type(faturamento))

faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))


# In[22]:


# Revisitando a motivação

"""
A empresa que você trabalha adquiriu uma startup de logística. Você precisa identificar todos endereços 
que são comuns a ambas. Na sua empresa, você armazena a latitude e longitude dos endereços em duas 
variáveis lat e lon, já a startup adquirida em uma unica variavel latlon.
"""


# In[26]:


posicao_char_divisao = latlon.find(";")
print(posicao_char_divisao)


# In[27]:


lat_startup = latlon[0:posicao_char_divisao]
print(lat_startup)


# In[28]:


lon_startup = latlon[posicao_char_divisao + 1:len(latlon)]
print(lon_startup)


# # Booleanos

# In[48]:


# Motivação

"""
Em websites (redes sociasis, e-commerce, corporativos etc) é comum o uso de sistemas
de controle de acesso, o famoso login. Em geral, nestes sistemas um usuário fornece dois dados: usuario e senha
"""

usuario = "tarcisio.almeida"
senha = "tarcisio123"

usuario_cadastro = "tarcisio.almeida"
senha_cadastro = "tarcisio"


# In[34]:


# Definição: True (verdadeiro) e False (falso)

verdadeiro = True
print(verdadeiro)


# In[33]:


falso = False
print(falso)


# In[35]:


print(type(True))


# In[36]:


# São resultados de comparações lógicas

"""
> (maior)
< (menor)
== (igual)
>= (maior ou igual)
<= (menor ou igual)
!= (diferente)
"""


# In[37]:


# Exemplo: Caixa eletrônico

saldo_em_conta = 200
valor_do_saque = 100

pode_executar_saque = valor_do_saque <= saldo_em_conta
print(pode_executar_saque)


# In[38]:


# Exemplo: cartão de crédito

codigo_de_seguranca = "852"
codigo_de_seguranca_cadastro = "010"

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)


# In[39]:


# Operações

"""
| (operador ou)
& (operador e)
not (operdor não)
"""


# In[40]:


# Exemplo: tabela verdade do operador | (ou)

print(True | True)
print(True | False)
print(False | False)
print(False | True)


# In[41]:


# Exemplo: tabela verdade do operador & (e)

print(True & True)
print(True & False)
print(False & False)
print(False & True)


# In[42]:


# Exemplo: tabela verdade do operador not (não)

print(not True)
print(not False)


# # Conversão

# In[43]:


idade = 29
tipo_sangue = "O+"
filhos = 0
telefone_fixo = None
telefone_fixo = ""

print(bool(idade))
print(bool(tipo_sangue))
print(bool(filhos))
print(bool(telefone_fixo))
print(bool(telefone_fixo))


# In[44]:


# Revisitando a motivação

"""
Em websites (redes sociasis, e-commerce, corporativos etc) é comum o uso de sistemas
de controle de acesso, o famoso login. Em geral, nestes sistemas um usuário fornece dois dados: usuario e senha
"""


# In[49]:


usuario_igual = usuario == usuario_cadastro
senha_igual = senha == senha_cadastro

print(usuario_igual)
print(senha_igual)


# In[51]:


conceder_acesso = usuario_igual & senha_igual
print(conceder_acesso)


# In[ ]:




