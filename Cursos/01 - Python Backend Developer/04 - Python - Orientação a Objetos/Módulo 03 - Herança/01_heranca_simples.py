# - - - - -> Herança Simples:

    #   A herança é um dos princípios fundamentais da POO, onde 
    # uma classe pode herdar atributos e métodos de outra classe,
    # promovendo a reutilização de código e estabelecendo relações 
    # entre as classes.


# - - - -> Exemplo de Herança Simples:

class Animal():  # Definindo a classe Pai (Superclasse):

    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Cachorro(Animal):  # Definindo uma classe Filha (Subclasse) que herda de 'Animal()'

    def fazer_som(self):
        return "Au au!"


class Gato(Animal):  # Definindo outra classe Filha (Subclasse) que herda de 'Animal()':

    def fazer_som(self):
        return "Miau!"


# - - -> Instânciando as Classes Filhas:  
cachorro = Cachorro("Rex")
gato = Gato("Whiskers")


# - - -> Utilizando o método '__str__()':
print()
print(cachorro)
print(gato)


# - - -> Utilizando o método 'fazer_som()':
print(f"\nNome: {cachorro.nome}, faz: {cachorro.fazer_som()}")
print(f"Nome: {gato.nome}, faz: {gato.fazer_som()}")
