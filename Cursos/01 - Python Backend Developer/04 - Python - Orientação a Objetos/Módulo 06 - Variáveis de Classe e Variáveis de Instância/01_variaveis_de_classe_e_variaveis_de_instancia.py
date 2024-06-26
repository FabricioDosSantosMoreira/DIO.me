# - - - - -> Variáveis de Classe e Variáveis de Instância:

    # - - - -> Variáveis de Classe:
        #   Variáveis ou atributos de classe são compartilhados por todas as 
        # instâncias da classe


    # - - - -> Variáveis de instância:
        #   Variáveis ou atributos de Instância são específicos de cada objeto 
        # criado a partir da class 


    # - - - -> Exemplo de Variáveis de Classe e Variáveis de Instância:
class Carro():

    
    fabricante = "Toyota"  # Variável de Classe
    
    def __init__(self, modelo, cor):
        
        self.modelo = modelo  # Variável de Instância
        self.cor = cor  # Variável de Instância


        # - - -> Criando Instâncias da Classe 'Carro()':
carro1 = Carro("Corolla", "Preto")
carro2 = Carro("Camry", "Branco")


        # - - -> Acessando Atributos de Classe:
print(f"\nAtributo 'fabricante' da Classe 'Carro()': \n\tFabricante: {Carro.fabricante}")


        # - - -> Acessando Atributos de Instância:
print(f"\nAtributos de Instância 'modelo' e 'cor' do Objeto 'carro1': \n\tModelo: {carro1.modelo} \n\tCor: {carro1.cor}")
print(f"\nAtributos de Instância 'modelo' e 'cor' do Objeto 'carro2': \n\tModelo: {carro2.modelo} \n\tCor: {carro2.cor}")


        # - - -> Modificando um Atributo de Classe:
carro1.fabricante = "Ferrari"  # Muda somente para o Objeto 'carro1'
print(f"\nAtributo 'fabricante' do Objeto 'carro1': \n\tFabricante: {carro1.fabricante}") 
print(f"Atributo 'fabricante' do Objeto 'carro2': \n\tFabricante: {carro2.fabricante}")

Carro.fabricante = "Porsche"  # Muda para todos os Objetos da Classe 'Carro()'
carro1 = Carro("Corolla", "Preto")
carro2 = Carro("Camry", "Branco")
print(f"\nAtributo 'fabricante' da Classe 'Carro()': \n\tFabricante: {Carro.fabricante}")
print(f"Atributo 'fabricante' do Objeto 'carro1': \n\tFabricante: {carro1.fabricante}")
print(f"Atributo 'fabricante' do Objeto 'carro2': \n\tFabricante: {carro2.fabricante}")
