# - - - - -> Escrita de Arquivos:

    #   A escrita de arquivos é um processo fundamental em muitos programas, pois permite 
    # armazenar dados permanentemente em dispositivos de armazenamento como disco rígido 
    # ou memória externa.


# - - - - -> Exemplo de Escrita de Arquivos:

# - - - -> Abrindo um arquivo em modo de escrita ('w'):
with open("./utils/exemplo.txt", "w", encoding='utf-8') as arquivo:

    arquivo.write("Exemplo de escrita de arquivo em Python usando 'write()'.\n")

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


# - - - -> Abrindo um arquivo em modo de adição ('a'):
with open("./utils/exemplo.txt", "a", encoding='utf-8') as arquivo:

    arquivo.write("\nEste texto será acrescentado ao arquivo existente.\n")
