# - - - - - > Classes Abstratas:
#                 Classes Abstratas são usadas para definir métodos que devem ser implementados 
#             por subclasses. Elas são úteis para garantir que as classes filhas tenham métodos 
#             específicos e para fornecer um contrato claro para a implementação.

#             NOTE: Por padrão, o Python não possui classes abstratas. Entretanto, o Python vem 
#             com um módulo que fornece a base para definir as classes abstratas, e o nome do 
#             módulo é ABC. O ABC funciona decorando métodos da classe base como abstratos e, 
#             em seguida, registrando classes concretas como implementações da base abstrata.

#             NOTE: Classes Abstratas apenas definem o que uma classe deve fazer e não como.


# - - - - > Classes Abstratas:
print("\nClasses Abstratas:")

from abc import ABC, abstractmethod

# - - - > Criando uma classe abstrata 'ControleRemoto' utilizando o múdulo 'ABC':
class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self) -> None:
        pass


    @abstractmethod
    def desligar(self) -> None:
        pass
    

    @property
    @abstractmethod
    def marca(self) -> str: 
        pass


# - - - > Criando uma subclasse 'ControleTV' que herda da classe abstrata 'ControleRemoto':
class ControleTV(ControleRemoto):   
    
    def __init__(self) -> None:
        print(f"Construtor chamado para criar um objeto da classe '{self.__class__.__name__}'")


    # NOTE: A classe 'ControleTV' deve implementar todos os métodos da classe abstrata 'ControleRemoto'
    def ligar(self) -> None:
        print("Ligando a TV...")
        print("Ligada!")


    def desligar(self) -> None:
        print("Desligando a TV...")
        print("Desligada!")


    @property
    def marca(self) -> str:
        return "Philco"


# - - - > Criando uma subclasse 'ControleArCondicionado' que herda da classe abstrata 'ControleRemoto':
class ControleArCondicionado(ControleRemoto):

    def __init__(self) -> None:
        print(f"Construtor chamado para criar um objeto da classe '{self.__class__.__name__}'")


    # NOTE: A classe 'ControleArCondicionado' deve implementar todos os métodos da classe abstrata 'ControleRemoto'
    def ligar(self) -> None:
        print("Ligando o Ar Condicionado...")
        print("Ligado!")


    def desligar(self) -> None:
        print("Desligando o Ar Condicionado...")
        print("Desligado!")


    @property
    def marca(self) -> str:
        return "LG"


# - - - > Tentando instanciar uma classe abstrata:
print("\nTentando instanciar uma classe abstrata:")
try:    
    # NOTE: Isso causará uma exceção 'TypeError'  
    controle_remoto = ControleRemoto()
except TypeError as exc:
    print(f"Resultado: {exc.__class__.__name__}")


# - - - > Criando instâncias das subclasses:
print("\nCriando instâncias das subclasses:")

controle_tv: ControleTV = ControleTV()
controle_ar: ControleArCondicionado = ControleArCondicionado()


# - - - > Acessando os métodos 'ligar()' e 'desligar()' das subclasses:
print("\nAcessando os métodos 'ligar()' e 'desligar()' das subclasses:")

controle_tv.ligar()
controle_tv.desligar()

controle_ar.ligar()
controle_ar.desligar()


# - - - > Acessando a propriedade 'marca' das subclasses:
print("\nAcessando a propriedade 'marca' das subclasses:")

print(f"Marca: {controle_tv.marca}")
print(f"Marca: {controle_ar.marca}")
