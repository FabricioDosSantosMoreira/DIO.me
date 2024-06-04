# - - - - -> Classes e Objetos:

    # - - - -> Classes:
        #   Uma classe é um modelo para objetos, descrevendo os 
        # atributos (dados) e métodos (comportamentos) que os 
        # objetos daquela classe terão. 
        

    # - - - -> Objetos:
        #   Os objetos são instâncias de classes, ou seja, são 
        # entidades individuais criadas com base no modelo 
        # definido pela classe.


    # - - - -> Exemplo de Classes e Objetos:


        # - - -> Definição da classe 'Pessoa()':
class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("\nOlá! Meu nome é", self.nome, "e tenho", self.idade, "anos.")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


        # - - -> Criando Objetos 'pessoa1' e 'pessoa2' (Instâncias da Classe):
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)


        # - - -> Acessando os atributos 'nome' e 'idade' dos objetos 'pessoa1' e 'pessoa2':
print("\nNome da pessoa1:", pessoa1.nome)
print("Idade da pessoa1:", pessoa1.idade)

print("\nNome da pessoa2:", pessoa2.nome)
print("Idade da pessoa2:", pessoa2.idade)


        # - - -> Acessando o método 'apresentar()' dos objetos 'pessoa1' e 'pessoa2':
pessoa1.apresentar()
pessoa2.apresentar()