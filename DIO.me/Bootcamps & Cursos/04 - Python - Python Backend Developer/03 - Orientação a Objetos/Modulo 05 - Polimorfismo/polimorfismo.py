# - - - - - > Polimorfismo:

#                 Polimorfismo é o princípio que permite que objetos de diferentes 
#             classes sejam tratados de maneira uniforme. Isso é alcançado por 
#             meio de herança e métodos com o mesmo nome em classes diferentes, 
#             mas com implementações específicas.


# - - - - > Exemplo de Polimorfismo:
print("\nExemplo de Polimorfismo:")

# - - - > Criando uma classe pai (superclasse) 'Animal':
class Animal(): 

    def __init__(self) -> None:
        print(f"Construtor chamado para criar um objeto da classe '{self.__class__.__name__}'")


    def falar(self) -> None:
        raise NotImplementedError("Subclasse deve implementar o método 'falar()'!")


# - - - > Criando uma classe filha (subclasse) 'Cachorro' que herda da classe 'Animal':
class Cachorro(Animal):
    
    def falar(self) -> str:
        return "O cachorro faz au au!"


# - - - > Criando uma classe filha (subclasse) 'Gato' que herda da classe 'Animal':
class Gato(Animal):  
    
    def falar(self) -> str:
        return "O gato faz miau!"


# - - - > Função genérica 'fazer_animal_falar()', que é independentemente da classe:
def fazer_animal_falar(animal: Animal) -> str:
    return animal.falar()


# - - - > Criando instâncias das classes filhas:
print("\nCriando instâncias das classes filhas:")

cachorro: Cachorro = Cachorro()
gato: Gato = Gato()


# - - - > Utilizando o método 'falar()' de cada instância:
print("\nUtilizando o método 'falar()' de cada instância:")

print(cachorro.falar())
print(gato.falar())


# - - - > Utilizando o método genérico 'fazer_animal_falar()' com cada instância:
print("\nUtilizando o método genérico 'fazer_animal_falar()' com cada instância:")

print(fazer_animal_falar(cachorro))
print(fazer_animal_falar(gato))
