# - - - - - > Herança Múltipla:
#                 A herança múltipla permite que uma classe herde atributos 
#             e métodos de várias classes base. Em Python, isso é alcançado 
#             listando as classes base entre parênteses na definição da classe.


# - - - - > Exemplo de Herança Múltipla:
print("\nExemplo de Herança Múltipla:")

# - - - > Criando uma classe base (superclasse) 'Animal':
class Animal():  

    def __init__(self, nome: str) -> None:
        self.nome: str = nome

        print(f"Construtor chamado para criar um objeto da classe '{self.__class__.__name__}' com o nome: {self.nome}")
    

    def emitir_som(self) -> None:
        pass


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# - - - > Criando uma classe base (superclasse) 'Mamifero':
class Mamifero():

    def __init__(self, cor_pelo: str) -> None:
        self.cor_pelo: str = cor_pelo
    

    def amamentar(self) -> None:
        pass


# - - - > Criando uma classe base (superclasse) 'Ave':
class Ave():

    def __init__(self, tipo_bico: str) -> None:
        self.tipo_bico: str = tipo_bico
    

    def voar(self) -> None:
        pass


# - - - > Criando uma classe derivada (subclasse) 'MamiferoVoador' que utiliza herança múltipla:
class MamiferoVoador(Animal, Mamifero, Ave):

    def __init__(self, nome: str, cor_pelo: str, tipo_bico: str) -> None:

        # NOTE: Chamando os construtores das classes base
        super().__init__(nome)  # NOTE: O mesmo que Animal.__init__(self, nome)
        Mamifero.__init__(self, cor_pelo)
        Ave.__init__(self, tipo_bico)
    

    def emitir_som(self) -> None:
        print("Mamífero voador está emitindo som!")


    def amamentar(self) -> None:
        print("Mamífero voador está amamentando!")


    def voar(self) -> None:
        print("Mamífero voador está voando!")


# - - - > Criando instâncias da classe derivada:
print("\nCriando instâncias da classe derivada:")

morcego: MamiferoVoador = MamiferoVoador("Morcego", "Marrom", "Pequeno")


# - - - > Acessando os atributos da instância:
print("\nAcessando os atributos da instância:")

print(f"Nome: {morcego.nome}")
print(f"Cor do pelo: {morcego.cor_pelo}")
print(f"Tipo de bico: {morcego.tipo_bico}")


# - - - > Acessando os métodos da instância:
print("\nAcessando os métodos da instância:")

morcego.emitir_som()
morcego.amamentar()
morcego.voar()


# - - - > Acessando o Method Resolution Order (MRO):
print("\nAcessando o Method Resolution Order (MRO):")

print(f"MRO da classe 'MamiferoVoador': {MamiferoVoador.__mro__}") 
print(f"MRO da classe 'MamiferoVoador': {MamiferoVoador.mro()}")
