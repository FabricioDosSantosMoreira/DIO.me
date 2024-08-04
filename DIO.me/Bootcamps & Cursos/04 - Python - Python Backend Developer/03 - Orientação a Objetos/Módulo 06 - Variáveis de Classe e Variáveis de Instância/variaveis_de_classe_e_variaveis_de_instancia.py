# - - - - - > Variáveis de Classe e Variáveis de Instância:

# - - - - > Variáveis de Classe:
#               Variáveis ou atributos de classe são compartilhados por todas as 
#           instâncias da classe. Qualquer mudança feita no atributo de classe é 
#           refletida em todas as instâncias que ainda não têm um atributo de 
#           instância com o mesmo nome.


# - - - - > Variáveis de instância:
#               Variáveis ou atributos de instância são específicos de cada objeto 
#           criado a partir da classe. Quando você define um atributo com o mesmo 
#           nome em uma instância, isso sobrescreve o atributo de classe para 
#           aquela instância.


# - - - -> Exemplo de Variáveis de Classe e Variáveis de Instância:
print("\nExemplo de Variáveis de Classe e Variáveis de Instância:")

# - - - > Criando uma classe 'Carro':
class Carro():

    fabricante: str = "Toyota"  # NOTE: Variável de Classe
    
    def __init__(self, modelo: str, cor: str) -> None:
        
        # NOTE: Variáveis de Instância
        self.modelo: str = modelo  
        self.cor: str = cor 

        print(f"Construtor chamado para criar um objeto da classe '{self.__class__.__name__}'")


# - - - > Criando instâncias da classe 'Carro':
print("\nCriando instâncias da classe 'Carro':")

carro_1 = Carro("Corolla", "Preto")
carro_2 = Carro("Camry", "Branco")


# - - - > Acessando o atributo 'fabricante' de classe:
print("\nAcessando o atributo 'fabricante' da classe:")

print(f"Fabricante: {Carro.fabricante}")


# - - - > Acessando os atributos 'modelo' e 'cor' de instância:
print("\nAcessando os atributos 'modelo' e 'cor' de instância:")

print(f"Modelo: {carro_1.modelo}, cor: {carro_1.cor}")
print(f"Modelo: {carro_2.modelo}, cor: {carro_2.cor}")


# - - - > Modificando o atributo de classe:
print("\nModificando o atributo de classe:")

carro_1.fabricante = "Ferrari"  # NOTE: Muda somente para o objeto 'carro_1' e se transforma em um atributo de instância

print(f"Fabricante: {carro_1.fabricante}")
print(f"Fabricante: {carro_2.fabricante}")

Carro.fabricante = "Porsche"  # NOTE: Muda para todos os objetos da classe 'Carro()' que possuem atributo de classe

print(f"Fabricante: {carro_1.fabricante}")
print(f"Fabricante: {carro_2.fabricante}")
