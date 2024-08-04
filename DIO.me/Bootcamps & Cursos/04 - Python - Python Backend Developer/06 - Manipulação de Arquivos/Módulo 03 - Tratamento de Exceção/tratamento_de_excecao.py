# - - - - - > Tratamento de Exceção:
#                 O tratamento de exceção em manipulação de arquivos é fundamental
#             para lidar com os possíveis problemas que podem ocorrer durante a 
#             leitura, escrita ou manipulação de arquivos. Isso ajuda a tornar 
#             o código mais robusto e a lidar de forma adequada com as 
#             exceções que possam surgir.


# - - - - > Exemplo de Tratamento de Erros:
print("\nExemplo de Tratamento de Erros:")

from pathlib import Path

ROOT_PATH: Path = Path(__file__).parent
caminho: Path = Path(ROOT_PATH / "util/lorem.txt")

try:
    arquivo = open(caminho, "r", encoding='utf-8')
    
    conteudo = arquivo.read()
    print(f"\nConteúdo do arquivo: \n{conteudo}")
    
    arquivo.close()

except IsADirectoryError as e: 
    print(f"\nErro de diretório (IsADirectoryError): {e}")

except FileNotFoundError as e:  
    print(f"\nErro de arquivo (FileNotFoundError): {e}")

except PermissionError as e:  
    print(f"\nErro de permisão: {e}")

except UnicodeDecodeError as e:
    print(f"\nErro de decodificação (DecodeError): {e}")

except UnicodeError as e: 
    print(f"\nErro de unicode (UnicodeError): {e}")

except IOError as e: 
    print(f"\nErro de E/S (IOError): {e}")
