arquivo = open('./lorem.txt', 'r')

#print(arquivo.read()) # Le todo o arquivo
#print(arquivo.readline()) # retorna linha a linha
#print(arquivo.readlines()) # retorna uma lista contendo as str de cada linha


# Tip
while len((linha := arquivo.readline())):
    print(linha)


arquivo.close()