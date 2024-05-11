# - - - - -> Polimorfismo:

    #   Polimorfismo é o princípio que permite que objetos de diferentes 
    # classes sejam tratados de maneira uniforme. Isso é alcançado por 
    # meio de herança e métodos com o mesmo nome em classes diferentes, 
    # mas com implementações específicas.


    # - - - -> Exemplo de Polimorfismo:
class Animal():  # Definição de uma Super Classe 'Animal()'

    def falar(self):
        raise NotImplementedError("\nSubclasse Deve Implementar o Método 'falar()'.")


class Cachorro(Animal):  # Definição da Classe 'Cachorro()', que herda de 'Animal()':
    
    def falar(self):
        return "O cachorro faz au au!"


class Gato(Animal):  # Definição da Classe 'Cachorro()', que herda de 'Animal()':
    
    def falar(self):
        return "O gato faz miau!"


    # - - - > Função Genérica 'falar()', Independentemente da Classe:
def fazer_animal_falar(animal):
    return animal.falar()


    # - - - > Criando Instâncias da Classe 'Cachorro()' e 'Gato()':
cachorro = Cachorro()
gato = Gato()


    # - - -> Utilizando o método 'falar()' do objeto 'cachorro' e 'gato':
print("\nUtilizando o Método 'falar()' da Classe 'Cachorro()': ", cachorro.falar())
print("Utilizando o Método 'falar()' da Classe 'Gato()': ", gato.falar())


    # - - -> Utilizando o método genérico 'fazer_animal_falar()' do objeto 'cachorro' e 'gato':
print("\nUtilizando o Método 'fazer_animal_falar()' com o Objeto 'cachorro': ", fazer_animal_falar(cachorro))
print("Utilizando o Método 'fazer_animal_falar()' com o Objeto 'gato': ", fazer_animal_falar(gato))
