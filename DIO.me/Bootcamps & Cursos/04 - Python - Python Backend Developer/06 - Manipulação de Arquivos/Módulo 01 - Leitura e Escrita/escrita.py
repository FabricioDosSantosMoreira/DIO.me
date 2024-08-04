# - - - - - > Escrita de Arquivos:

#                 A escrita de arquivos é um processo fundamental em muitos programas, 
#             pois permite armazenar dados permanentemente em dispositivos de 
#             armazenamento como disco rígido  ou memória externa.


# - - - - -> Exemplos de Escrita de Arquivos:
print("\nExemplos de Escrita de Arquivos:")

# - - - > Abrindo um Arquivo em Modo de Escrita ('w'):
print("\nAbrindo um Arquivo em Modo de Escrita ('w'):")

caminho: str = "./util/texto.txt"

with open(caminho, 'w', encoding='utf-8') as arquivo:

    arquivo.write("\nExemplo de escrita de arquivo em Python usando 'write()'.\n")

    arquivo.writelines(
        [
            'Exemplo ',
            'de ',
            'escrita ',
            'de ',
            'arquivos ',
            'em ',
            'Python ',
            'usando ',
            "'writelines()'.",
        ]
    )


# - - - > Abrindo um Arquivo em Modo de Adição ('a'):
print("\nAbrindo um Arquivo em Modo de Adição ('a'):")

caminho: str = "./util/texto.txt"

with open(caminho, 'a', encoding='utf-8') as arquivo:

    arquivo.write("\nEste texto será acrescentado ao arquivo existente.\n")
