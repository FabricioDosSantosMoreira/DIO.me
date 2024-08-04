# - - - - - > Escrita de Arquivos:
#                 A escrita de arquivos é um processo fundamental em muitos programas, 
#             pois permite armazenar dados permanentemente em dispositivos de 
#             armazenamento como disco rígido  ou memória externa.


# - - - - -> Exemplos de Escrita de Arquivos:
print("\nExemplos de Escrita de Arquivos:")

from pathlib import Path

ROOT_PATH: Path = Path(__file__).parent
caminho: Path = Path(ROOT_PATH / "util/escrita.txt")

# - - - > Abrindo um Arquivo em Modo de Escrita ('w'):
print("\nAbrindo um Arquivo em Modo de Escrita ('w'):")

with open(caminho, 'w', encoding='utf-8') as arquivo:

    arquivo.write("Exemplo de escrita de arquivo em Python usando 'write()'.")

    arquivo.writelines(
        [
            "\nExemplo ",
            "de ",
            "escrita ",
            "de ",
            "arquivos ",
            "em ",
            "Python ",
            "usando ",
            "'writelines()'.",
        ]
    )


# - - - > Abrindo um Arquivo em Modo de Adição ('a'):
print("\nAbrindo um Arquivo em Modo de Adição ('a'):")

with open(caminho, 'a', encoding='utf-8') as arquivo:

    arquivo.write("\nEste texto será acrescentado ao arquivo existente.")
