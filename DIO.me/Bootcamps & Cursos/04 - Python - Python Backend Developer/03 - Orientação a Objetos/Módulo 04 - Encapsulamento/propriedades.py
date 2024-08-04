#  - - - - - > Propriedades:

#                  Com o property do Python, você pode criar atributos
#              gerenciados em suas classes. Esses atributos são também 
#              conhecidos como propriedades.Propriedades permitem que 
#              você defina métodos para acessar e modificar um 
#              atributo, dando controle sobre seu comportamento 
#              de leitura, escrita e exclusão.


# - - - - > Exemplos de Propriedade:
print("\nExemplos de Propriedade:")

# - - - > Criando uma classe 'Foo':
class Foo():

    def __init__(self, x: int=0) -> None:
        self._x: int = x


    # NOTE: Declara o atributo 'x' como uma propriedade
    @property
    def x(self) -> None:
        pass
    
    
    #NOTE: Propriedade 'getter' para o atributo 'x'. Retorna o valor atual de '_x'.
    @x.getter
    def x(self) -> int:
        print("Propriedade 'getter' acessada!")
        return self._x
    

    # NOTE: Propriedade 'setter' para o atributo 'x'. Adiciona o valor especificado ao valor atual de '_x'
    @x.setter
    def x(self, value) -> None:
        print("Propriedade 'setter' acessada!")
        self._x += value


    #NOTE: Propriedade 'deleter' para o atributo 'x'. Define o valor de '_x' como 0, excluindo assim seu valor atual. 
    @x.deleter
    def x(self) -> None:
        print("Propriedade 'deleter' acessada!")
        self._x = 0


# - - - > Criando uma instância da classe 'Foo':
print("\nCriando uma instância da classe 'Foo':")

foo: Foo = Foo(10)


# - - - > Acessando as propriedades da instância:
print("\nAcessando as propriedades da instância:")

print(f"Instância 'foo.x': {foo.x}\n")  # NOTE: Acessa @x.getter


foo.x = 10  # NOTE: Acessa @x.setter
print(f"Instância 'foo.x': {foo.x}\n")  # NOTE: Acessa @x.getter


del foo.x  # NOTE: Acessa @x.deleter
print(f"Instância 'foo.x': {foo.x}\n")  # NOTE: Acessa @x.getter
