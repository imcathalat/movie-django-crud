import json

arquivo = open('oscar_awards.txt', 'r')
linhas = arquivo.readlines()
quant_linhas = len(linhas)

lista = []
dicionario = {}

for i, linha in enumerate(linhas):
    dicionario = {str(i+1): linha.strip()}

    lista.append(dicionario)

print(lista)


json_oscar_file = open('oscar_awards_json.json', 'w')
converted_for_json = json.dump(lista, json_oscar_file )


# for i in json_oscar_file:
#     json_oscar_file.write(converted_for_json)