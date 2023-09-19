# Definição
"Armazenam sequências imutáveis e desordenadas valores, sem repetição. São do tipo set:"

frutas = {"banana", "maca", "uva", "uva"}
print(frutas)
print(type(frutas))

# Operações
"As operações da estrutura do tipo set são:"
"- (diferença)"
"Ex.: países da Europa"

norte_europa = {"reuno unido", "suecia", "russia", "noruega", "dinamarca"}
escandinavia = {"noruega", "dinamarca", "suecia"}

norte_europa_nao_escandinavo = norte_europa - escandinavia
print(norte_europa_nao_escandinavo)

escandinavo_nao_norte_europa = escandinavia - norte_europa
print(escandinavo_nao_norte_europa)

# Métodos
"São métodos nativos do Python que nos ajudam a trabalhar no dia a dia em conjuntos."

cursos = {"Exatas", "Humanas", "Biológicas"}
print(cursos)

# inserir um elemento no conjunto: set.add(valo)
cursos.add("Saúde")
print(cursos)

# remover um elemento no conjunto: set.remove(val)
cursos.remove("Saúde")
print(cursos)

# Conversão
"Podemos converter conjuntos para lista e vice e versa"

times_paulistas = {"São Paulo", "Palmeiras", "Corinthians", "Santos"}
print(list(times_paulistas))
print(type(list(times_paulistas)))

# Revisitando a motivação
"Você trabalha como analista de dados de mídias sociais e precisa descobrir todas as hastags que alcançaram o top trending do Twitter durante uma semana. Você já conseguiu as hastags por dia da semana:"
hastags_seg = ["#tiago", "#joao", "#bbb"]
hastags_ter = ["#sarah", "#bbb", "#fiuk"]
hastags_qua = ["#gil", "#thelma", "#lourdes"]
hastags_qui = ["#rafa", "#fora", "#danilo"]
hastags_sex = ["#juliete", "#arthur", "#bbb"]

hastags_semana = hastags_seg + hastags_ter + hastags_qua + hastags_qui + hastags_sex
print(hastags_semana)
print(len(hastags_semana))

hastags_semana = list(set(hastags_seg + hastags_ter + hastags_qua + hastags_qui + hastags_sex))
print(hastags_semana)
print(len(hastags_semana))