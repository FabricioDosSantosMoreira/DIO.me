# - - - - -> Encapsulamento:

    #   Em programação orientada a objetos, o encapsulamento é um 
    # conceito que permite ocultar detalhes internos de um objeto
    # e expor apenas as operações relevantes para seu uso externo. 
    # Isso é alcançado através do uso de métodos e atributos privados.


# - - - -> Exemplo de Encapsulamento: 
class Carro():

    def __init__(self, marca, modelo, ano):
        self.__marca = marca    # Atributo privado
        self.__modelo = modelo  # Atributo privado
        self.__ano = ano        # Atributo privado
        self.__ligado = False   # Atributo privado 

    def ligar(self):
        if not self.__ligado:
            print("\nO carro está ligando...")
            self.__ligado = True
        else:
            print("\nO carro já está ligado!")
    
    def desligar(self):
        if self.__ligado:
            print("\nO carro está desligando...")
            self.__ligado = False
        else:
            print("\nO carro já está desligado!")
    
    def info_carro(self):
        print("\nMarca:", self.__marca)
        print("Modelo:", self.__modelo)
        print("Ano:", self.__ano)
        print("Status:", "ligado" if self.__ligado else "desligado")

    @property
    def anos_de_uso(self):  # Atibutos Gerenciados
        from datetime import datetime
        __ano_atual = datetime.now().year

        return __ano_atual - self.__ano


    # - - -> Criando um Objeto da Classe 'Carro()':
meu_carro = Carro("Toyota", "Corolla", 2022)


    # - - -> Tentando acessar o atributo privado '__marca' diretamente:
try:
    print(f"\nMarca: {meu_carro.__marca}")  # NOTE: Isso causará raise AttributeError
except AttributeError as e:
    print(f"\nTentando acessar o atributo privado '__marca' diretamente: \n\tResultado: {e.__class__.__name__}")


    # - - -> Utilizando os métodos do objeto 'meu_carro':
meu_carro.ligar()
meu_carro.info_carro()
meu_carro.desligar()
meu_carro.info_carro()


    # - - -> Utilizando a propriedade 'anos_de_uso' do objeto 'meu_carro':
print(f"\nAnos de uso: {meu_carro.anos_de_uso}")
