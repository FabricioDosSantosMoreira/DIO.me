# - - - - -> Classes Abstratas:

    # Classes Abstratas são usadas para definir métodos que devem ser implementados por 
    #   subclasses. Elas são úteis para garantir que as classes filhas tenham métodos 
    #   específicos e para fornecer um contrato claro para a implementação.


    # NOTE: Por padrão, o Python não possui classes abstratas. Entretanto, o Python vem 
    #   com um módulo que fornece a base para definir as classes abstratas, e o nome do 
    #   módulo é ABC. O ABC funciona decorando métodos da classe base como abstratos e, 
    #   em seguida, registrando classes concretas como implementações da base abstrata.

    # NOTE: Classes Abstratas apenas definem o que uma classe deve fazer e não como.


    # - - - -> Exemplo de implementação de uma classe abstrata:
from abc import ABC, abstractmethod


class ControleRemoto(ABC):  # Implementação de Classe Abstrata utilizando o múdulo 'ABC'

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self): 
        pass


class ControleTV(ControleRemoto): # Implementação de Subclasse 'ControleTV()'
    
    def ligar(self):
        print("\nLigando a TV...")
        print("\nLigada!")

    def desligar(self):
        print("\nDesligando a TV...")
        print("\nDesligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto): # Implementação de Subclasse 'ControleArCondicionado()'
    def ligar(self):
        print("\nLigando o Ar Condicionado...")
        print("\nLigado!")

    def desligar(self):
        print("\nDesligando o Ar Condicionado...")
        print("\nDesligado!")

    @property
    def marca(self):
        return "LG"
#


    # - - - -> Utilização das classes:

        # - - -> Tentando Instanciar uma Classe Abstrata:
try:
    controle_remoto = ControleRemoto() # NOTE: raise TypeError
except TypeError as e:
    print(f"\nTentando Instanciar uma Classe Abstrata: \n\tResultado: {e.__class__.__name__}")


        # - - -> Instanciando Subclasses:
controle_tv = ControleTV()
controle_ar = ControleArCondicionado()


print("\nChamando os Métodos 'ligar()' e 'desligar()' da Subclasse 'ControleTV()':")
controle_tv.ligar()
controle_tv.desligar()
print(f"\nChamando a Propriedade 'marca' da Subclasse 'ControleTV()': \n\tMarca: {controle_tv.marca}")


print("\nChamando os Métodos 'ligar()' e 'desligar()' da Subclasse 'ControleArCondicionado()':")
controle_ar.ligar()
controle_ar.desligar()

print(f"\nChamando a Propriedade 'marca' da Subclasse 'ControleArCondicionado()': \n\tMarca: {controle_ar.marca}")
