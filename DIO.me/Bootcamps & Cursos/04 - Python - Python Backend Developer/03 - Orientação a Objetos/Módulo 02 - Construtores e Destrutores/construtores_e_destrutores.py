# - - - - - > Construtores e Destrutores:
#                 Construtores e destrutores são métodos especiais em programação 
#             que são usados para inicializar e liberar recursos de um objeto, 
#             respectivamente. Eles desempenham um papel importante na gestão
#             de memória e na inicialização de objetos.


# - - - - > Exemplo de Construtores e Destrutores:
print("\nExemplo de Construtores e Destrutores:")

# - - - > Criando uma classe 'Pessoa':
class Pessoa():

    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

        print(f"Construtor chamado para criar um objeto com o nome: {self.nome}")


    def __del__(self) -> None:
        print(f"Destrutor chamado para excluir um objeto com nome: {self.nome}")


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# - - - > Criando instâncias da classe 'Pessoa':
print("\nCriando instâncias da classe 'Pessoa':")

pessoa_1: Pessoa = Pessoa("João", 30)
pessoa_2: Pessoa = Pessoa("Maria", 25)


# - - - > Deletando instâncias da classe 'Pessoa':
print("\nDeletando instâncias da classe 'Pessoa':")

del pessoa_1
del pessoa_2


# - - - > Tentando acessar a instância já deletada:
print("\nTentando acessar a instância já deletada:")

try:
    # NOTE: Isso causará uma exceção 'NameError'  
    print(pessoa_1)
except NameError as exc:
    print(f"Resultado: {exc.__class__.__name__}")
