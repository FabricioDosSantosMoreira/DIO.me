# - - - - -> Construtores e Destruidores

    #   Construtores e destrutores são métodos especiais em programação 
    # que são usados para inicializar e liberar recursos de um objeto, 
    # respectivamente. Eles desempenham um papel importante na gestão de 
    # memória e na inicialização de objetos.


    # - - - -> Exemplo de Construtores e Destrutores:


        # - - -> Definição da classe 'Pessoa()':
class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print("\nConstrutor chamado para criar: ", self.nome)

    def __del__(self):
        print("\nDestrutor chamado para excluir: ", self.nome)


        # - - -> Criando objetos 'pessoa1' e 'pessoa2' (Instâncias da Classe):
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)


        # - - -> Deletando objetos 'pessoa1' e 'pessoa2':
del pessoa1
del pessoa2


        # - - -> Tentando acessar o objeto 'pessoa1' já deletado:
try:
    print(pessoa1)
except NameError as e:
    print(f"\nTentando acessar o objeto pessoa1 já deletado: \n\tResultado: {e.__class__.__name__}")
