# - - - - - > Encapsulamento:

#                 Em programação orientada a objetos, o encapsulamento é um 
#             conceito que permite ocultar detalhes internos de um objeto
#             e expor apenas as operações relevantes para seu uso externo. 
#             Isso é alcançado através do uso de métodos e atributos privados.


# - - - - > Exemplo de Encapsulamento: 
print("\nExemplo de Encapsulamento:")

# - - - > Criando uma classe 'Carro':
class Carro():

    def __init__(self, ano: int, marca: str, modelo: str) -> None:

        # NOTE: Atributos privados
        self.__ano: int = ano       
        self.__marca: str = marca   
        self.__modelo: str = modelo 
        self.__ligado: bool = False  

        print(f"Construtor chamado para criar um objeto da classe '{self.__class__.__name__}'")


    def ligar(self) -> None:
        if not self.__ligado:
            print("O carro está ligando...")
            self.__ligado = True
        else:
            print("O carro já está ligado!")
    

    def desligar(self) -> None:
        if self.__ligado:
            print("O carro está desligando...")
            self.__ligado = False
        else:
            print("O carro já está desligado!")
    

    def info_carro(self) -> None:
        print(
            f'''Ano: {self.__ano}, Marca: {self.__marca}, Modelo: {self.__modelo}, Status: {"ligado" if self.__ligado else "desligado"}'''
        )

    # NOTE: Atributos gerenciados
    @property
    def anos_de_uso(self) -> int: 

        from datetime import datetime
        __ano_atual: int = datetime.now().year

        return __ano_atual - self.__ano


# - - - > Criando uma instância da classe 'Carro':
print("\nCriando uma instância da classe 'Carro':")

carro: Carro = Carro(2022, "Toyota", "Corolla")


# - - - > Tentando acessar o atributo privado '__marca' diretamente:
print("\nTentando acessar o atributo privado '__marca' diretamente:")

try:
    # NOTE: Isso causará uma exceção 'AttributeError'  
    print(f"Marca: {carro.__marca}")
except AttributeError as e:
    print(f"Resultado: {e.__class__.__name__}")


# - - - > Acessando os métodos da instância:
print("\nAcessando os métodos da instância:")

carro.ligar()
carro.info_carro()
carro.ligar()

carro.desligar()
carro.info_carro()
carro.desligar()


# - - - > Acessando a propriedade 'anos_de_uso' da instância:
print("\nAcessando a propriedade 'anos_de_uso' da instância:")

print(f"Anos de uso: {carro.anos_de_uso}")
