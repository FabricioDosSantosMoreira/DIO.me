# - - - - -> Herança Múltipla:

    #   A herança múltipla permite que uma classe herde atributos 
    # e métodos de várias classes base. Em Python, isso é alcançado 
    # listando as classes base entre parênteses na definição da classe.


# - - - -> Exemplo de Herança Múltipla:

# - - -> Definindo as classes base:
class Animal():  
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero():
    def __init__(self, cor_pelo):
        self.cor_pelo = cor_pelo
    
    def amamentar(self):
        pass

class Ave():
    def __init__(self, tipo_bico):
        self.tipo_bico = tipo_bico
    
    def voar(self):
        pass


# - - -> Definindo a classe derivada com herança múltipla:
class MamiferoVoador(Animal, Mamifero, Ave):

    def __init__(self, nome, cor_pelo, tipo_bico):

        # Chamando os construtores das classes base
        super().__init__(nome)  # Animal.__init__(self, nome)
        Mamifero.__init__(self, cor_pelo)
        Ave.__init__(self, tipo_bico)
    
    def emitir_som(self):
        print("\nSom de mamífero voador")

    def amamentar(self):
        print("\nMamífero voador amamentando")

    def voar(self):
        print("\nMamífero voador voando")


# - - -> Instânciando da classe derivada:

morcego = MamiferoVoador("Morcego", "Marrom", "Pequeno")


# - - -> Acessando atributos da instância:
print(f"\nNome: {morcego.nome}")
print(f"Cor do pelo: {morcego.cor_pelo}")
print(f"Tipo de bico: {morcego.tipo_bico}")


# - - -> Acessando métodos da instância:
morcego.emitir_som()
morcego.amamentar()
morcego.voar()


# Acessando o Method Resolution Order (MRO):
print(f"\nMRO da classe MamiferoVoador: {MamiferoVoador.__mro__}") 
print(f"MRO da classe MamiferoVoador: {MamiferoVoador.mro()}")