# - - - - -> Métodos de Classe e Métodos Estáticos:

    # - - - -> Métodos de Classe: 
        #   Métodos de classe estão ligados à classe e não ao objeto. 
        # Eles têm acesso ao estado da classe, pois recebem um parâmetro que 
        # aponta para a classe e não para a instância do objeto.


    # - - - -> Métodos Estáticos: 
        #   Um método estático não recebe um primeiro argumento explícito. 
        # Ele também é um método vinculado à classe e não ao objeto da classe. 
        # Este método não pode acessar ou modificar o estado da classe.


    # - - - -> Exemplo de Classe com Método Estático:
class Calculadora():

    @staticmethod  # Método Estático
    def soma(a, b):
        return a + b
    
    @staticmethod  # Método Estático
    def multiplica(a, b):
        return a * b

resultado = Calculadora.soma(5, 5)
print(f"\nMétodo Estático soma(5, 5) da Classe 'Calculadora()': \n\tResultado: {resultado}")  # Saída: 10

resultado = Calculadora.multiplica(3, 5) 
print(f"\nMétodo Estático 'multiplica(3, 5)' da Classe 'Calculadora()': \n\tResultado: {resultado}")  # Saída: 15


    # - - - -> Exemplo de Classe com Método de Classe:
class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # Método de Classe
    def criar_de_ano_nascimento(cls, ano, nome):

        from datetime import datetime
        ANO_ATUAL = datetime.now().year

        idade = ANO_ATUAL - ano
        return cls(nome, idade)

pessoa = Pessoa.criar_de_ano_nascimento(2005, 'Fabrício')
print(f"""\nMétodo de Classe 'criar_de_ano_nascimento(2005, 'Fabrício')' da Classe 'Pessoa()': 
      \tNome: {pessoa.nome} 
      \tIdade: {pessoa.idade}""")
