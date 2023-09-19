#!/usr/bin/env python
# coding: utf-8

# # Listas

# In[4]:


# Motivação

print("O aplicativo do seu banco registra toda a sua movimentação financeira. Ao final do dia, o app consolida o saldo final para que você possa controlar sua vida financeira.")


# In[5]:


dia_11_saldo_inicial = 1000


# In[6]:


dia_11_transacao_1 = 243
dia_11_transacao_2 = -798.58
dia_11_transacao_3 = 427.12
dia_11_transacao_4 = -10.91


# In[10]:


dia_11_saldo_final = dia_11_saldo_inicial + dia_11_transacao_1 + dia_11_transacao_2 + dia_11_transacao_3 + dia_11_transacao_4


# In[11]:


print(dia_11_saldo_final)


# In[13]:


# Definição: armazenam sequências mutáveis e ordenadas de valores. São do tipo list.

usuario_web = ["Tarcísio Almeida", "tarcisio.almeida", "tarcisio.almeidabh@outlook.com"]
print(usuario_web)
print(type(usuario_web))


# In[16]:


idade = 28
saldo_em_conta = 723.15
usuario_loggedin = True

usuario_web = ["Tarcísio Almeida", idade, "tarcisio.almeida", "tarcisio.almeidabh@outlook.com", saldo_em_conta, usuario_loggedin]
print(usuario_web)
print(type(usuario_web))


# In[17]:


# Operações: As operações da estrutura do tipo list são: + (concatenação)


# In[18]:


# Exemplo: Fabricantes de hardware mobile

fabricantes_mobile_china = ["xiaomi", "huawei"]
fabricantes_mobile_eua =  ["apple", "motorola"]
fabricantes_mobile = fabricantes_mobile_china + fabricantes_mobile_eua

print(fabricantes_mobile_china)
print(fabricantes_mobile_eua)
print(fabricantes_mobile)


# In[19]:


# Outra operação muito utilizada é a de fatiamento (slicing), semelhante ao de strings.


# In[21]:


# Fatiamento fixo

print(f"0: {fabricantes_mobile[0]}")
print(f"0: {fabricantes_mobile[-1]}")


# In[22]:


#Fatiamento por intervalo

fabricantes_mobile_china = fabricantes_mobile[0:2]
fabricantes_mobile_eua = fabricantes_mobile[2:len(fabricantes_mobile)]

print("china: " + str(fabricantes_mobile_china))
print("eua: " + str(fabricantes_mobile_eua))


# In[24]:


# Podemos adicionar elementos a uma posição específica da lista

print(fabricantes_mobile)

fabricantes_mobile[2] = "nokia"
print(fabricantes_mobile)


# In[25]:


# Métodos: São métodos nativos do Python que nos ajudam a trabalhar no dia a dia com listas.


# In[26]:


juros = [0.05, 0.07, 0.02, 0.04, 0.08]


# In[27]:


# inserir um elemento sem substituir: list.insert(index, val)
juros.insert(0, 0.10)
print(juros)


# In[29]:


# inserir um elemento no fim da lista: list.append(val)
juros.append(0.09)
print(juros)


# In[30]:


# remover um elemento pelo valor: list.remove(val)
juros.remove(0.1)
print(juros)


# In[32]:


# remover um elemento pelo índice: list.remove(val)
terceiro_juros= juros.pop(2)
print(terceiro_juros)


# In[33]:


print(juros)


# In[34]:


# Conversão: Podemos converter alguns tipos de variáveis em listas, como strings.

email = "tarcisioalmeidabh@outlook.com"
caracteres_email = list(email)

print(email)
print(caracteres_email)


# In[35]:


# Revisitando a motivação

print("O aplicativo do seu banco registra toda a sua movimentação financeira. Ao final do dia, o app consolida o saldo final para que você possa controlar sua vida financeira.")


# In[37]:


dia_11_transacoes = []

dia_11_transacoes.append(243)
dia_11_transacoes.append(-798.58)
dia_11_transacoes.append(427.12)
dia_11_transacoes.append(-10.91)

print(dia_11_transacoes)


# In[41]:


dia_11_saldo_final = dia_11_saldo_inicial + dia_11_transacoes[0] + dia_11_transacoes[1] + dia_11_transacoes[2] + dia_11_transacoes[3]
print(dia_11_saldo_final)


# # Conjuntos

# In[1]:


# Motivação

print("Você trabalha como analista de dados de mídias sociais e precisa descobrir todas as hastags que alcançaram o top trending do Twitter durante uma semana. Você já conseguiu as hastags por dia da semana:")


# In[2]:


hastags_seg = ["#tiago", "#joao", "#bbb"]
hastags_ter = ["#sarah", "#bbb", "#fiuk"]
hastags_qua = ["#gil", "#thelma", "#lourdes"]
hastags_qui = ["#rafa", "#fora", "#danilo"]
hastags_sex = ["#juliete", "#arthur", "#bbb"]


# In[5]:


print("Uma simples concatenação de listas fará com que a hastag #bbb, entre outras, apareça mais de uma vez.")
hastags_semana = hastags_seg + hastags_ter + hastags_qua + hastags_qui + hastags_sex
print(hastags_semana)


# In[ ]:




