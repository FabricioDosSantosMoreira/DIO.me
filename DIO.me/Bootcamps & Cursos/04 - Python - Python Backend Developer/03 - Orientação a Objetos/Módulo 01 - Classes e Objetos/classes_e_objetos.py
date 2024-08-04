# - - - - - > Classes e Objetos:

# - - - - > Classes:

#               Uma classe é um modelo para objetos, descrevendo os 
#           atributos (dados) e métodos (comportamentos) que os 
#           objetos daquela classe terão. 
        
# - - - - > Objetos:

#               Os objetos são instâncias de classes, ou seja, são 
#           entidades individuais criadas com base no modelo 
#           definido pela classe.


# - - - - > Exemplo de Classes e Objetos:
print("\nExemplo de Classes e Objetos:")


# - - - > Criando uma classe 'Pessoa':
class Pessoa():

    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

        print("Objeto da classe 'Pessoa' criado!")


    def apresentar(self) -> None:
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# - - - > Criando instâncias ou objetos da classe 'Pessoa':
print("\nCriando instâncias ou objetos da classe 'Pessoa':")

pessoa_1: Pessoa = Pessoa("João", 30)
pessoa_2: Pessoa = Pessoa("Maria", 25)


# - - - > Acessando os atributos 'nome' e 'idade' dos objetos:
print("\nAcessando os atributos 'nome' e 'idade' dos objetos:")

print(f"Nome: {pessoa_1.nome}")
print(f"Idade: {pessoa_1.idade}")

print(f"Nome: {pessoa_2.nome}")
print(f"Idade: {pessoa_2.idade}")


# - - - > Acessando o método 'apresentar()' dos objetos:
print("\nAcessando o método 'apresentar()' dos objetos:")

pessoa_1.apresentar()
pessoa_2.apresentar()
