arquivo = open('./teste_escrita.txt', 'w')

arquivo.write('Escrevendo dados em um novo arquivo!')

arquivo.writelines([
                    '\npython ',
                    '\nEscrevendo ',
                    'um ',
                    'novo ',
                    'texto ',
                    ])



arquivo.close()