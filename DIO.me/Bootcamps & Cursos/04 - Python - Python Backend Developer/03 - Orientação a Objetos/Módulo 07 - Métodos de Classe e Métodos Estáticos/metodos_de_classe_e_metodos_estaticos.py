# - - - - - > Métodos de Classe e Métodos Estáticos:

# - - - - > Métodos Estáticos: 
#               Um método estático não recebe um primeiro argumento explícito. 
#           Ele também é um método vinculado à classe e não ao objeto da classe. 
#           Este método não pode acessar ou modificar o estado da classe.


# - - - - > Métodos de Classe: 

#               Métodos de classe estão ligados à classe e não ao objeto. 
#           Eles têm acesso ao estado da classe, pois recebem um parâmetro que 
#           aponta para a classe e não para a instância do objeto.


# - - - - > Exemplos de Métodos Estáticos e Métodos de Classe:
print("\nExemplos de Métodos Estáticos e Métodos de Classe:")

# - - - > Criando uma classe 'Calculadora' que possue métodos estáticos:
class Calculadora():

    # NOTE: Métodos estáticos
    @staticmethod  
    def soma(a: float, b: float) -> float:
        print(f"O método estático '{__class__.soma.__name__}' foi acessado!")
        print(f"valores: a={a}, b={b}")
        return a + b
    

    @staticmethod
    def multiplica(a: float, b: float) -> float:
        print(f"O método estático '{__class__.multiplica.__name__}' foi acessado!")
        print(f"valores: a={a}, b={b}")
        return a * b


# - - - > Acessando os métodos estáticos 'soma()' e 'multiplica()' da classe 'Calculadora':
print("\nAcessando os métodos estáticos 'soma()' e 'multiplica()' da classe 'Calculadora':")

resultado: float = Calculadora.soma(5.0, 6.7)
print(f"Resultado: {resultado}")

resultado: float = Calculadora.multiplica(3.5, 9) 
print(f"Resultado: {resultado}") 



# - - - - > Criando uma classe 'Calculadora' que possue método de classe:
class Pessoa():

    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

        print(f"Construtor chamado para criar um objeto da classe '{self.__class__.__name__}'")


    # NOTE: Método de classe
    @classmethod 
    def criar_de_ano_nascimento(cls, nome: str,  ano_nascimento: int) -> 'Pessoa':
        from datetime import datetime

        ano_atual: int = datetime.now().year
        idade: int = ano_atual - ano_nascimento

        return cls(nome=nome, idade=idade)


# - - - > Acessando o método de classe 'criar_de_ano_nascimento()' da classe 'Pessoa':
print("\nAcessando o método de classe 'criar_de_ano_nascimento()' da classe 'Pessoa':")

pessoa: Pessoa = Pessoa.criar_de_ano_nascimento("Fabrício", 2005)
print(f"Nome: {pessoa.nome}, idade: {pessoa.idade}")
