# - - - - - > Herança Simples:

#                 A herança é um dos princípios fundamentais da POO, onde 
#             uma classe pode herdar atributos e métodos de outra classe,
#             promovendo a reutilização de código e estabelecendo relações 
#             entre as classes.


# - - - - > Exemplo de Herança Simples:
print("\nExemplo de Herança Simples:")

# - - - > Criando uma classe pai (superclasse) 'Animal':
class Animal(): 

    def __init__(self, nome: str) -> None:
        self.nome: str = nome

        print(f"Construtor chamado para criar um objeto da classe '{self.__class__.__name__}' com o nome: {self.nome}")


    def fazer_som(self) -> str:
        pass


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# - - - > Criando uma classe filha (subclasse) 'Cachorro' que herda da classe 'Animal':
class Cachorro(Animal):  

    def fazer_som(self) -> str:
        return "Au au!"


# - - - > Criando uma classe filha (subclasse) 'Gato' que herda da classe 'Animal':
class Gato(Animal):

    def fazer_som(self) -> str:
        return "Miau!"


# - - - > Criando instâncias das classes filhas:
print("\nCriando instâncias das classes filhas:")

cachorro: Cachorro = Cachorro("Cookie")
gato: Gato = Gato("Paçoca")


# - - - > Utilizando o método '__str__()':
print("\nUtilizando o método '__str__()':")

print(cachorro)
print(gato)


# - - - > Utilizando o método 'fazer_som()':
print("\nUtilizando o método 'fazer_som()':")

print(f"Nome: {cachorro.nome}, faz: {cachorro.fazer_som()}")
print(f"Nome: {gato.nome}, faz: {gato.fazer_som()}")
