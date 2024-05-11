#  - - - - -> Propriedade:

    #   Com o property() do Python, você pode criar atributos
    # gerenciados em suas classes. Esses atributos são também 
    # conhecidos como propriedades.Propriedades permitem que 
    # você defina métodos para acessar e modificar um 
    # atributo, dando controle sobre seu comportamento 
    # de leitura, escrita e exclusão.


    # - - - -> Exemplo de Propriedade:
class Foo():

    def __init__(self, x=None):
        self._x = x

    # Método 'getter' para o atributo 'x'.
    # Retorna o valor de '_x' se existir, caso contrário, retorna 0.
    @property
    def x(self):
        return self._x or 0
    
    # Método 'setter' para o atributo 'x'.
    # Adiciona o valor especificado ao valor atual de '_x'.
    @x.setter
    def x(self, value):
        print("\nSetter")
        self._x += value

    # Outro método getter para o atributo 'x'.
    # Retorna o valor atual de '_x'.
    @x.getter
    def x(self):
        print("\nGetter")
        return self._x

    # Método deleter para o atributo 'x'.
    # Define o valor de '_x' como 0, excluindo assim seu valor atual. 
    @x.deleter
    def x(self):
        print("\nDeleter")
        self._x = 0

    
   
    # - - -> Instânciando um objeto da classe 'Foo()':
foo = Foo(10)


    # - - -> Utilizando as propriedades:
print(f"foo.x: {foo.x}")  # @x.getter

foo.x = 10  # @x.setter

print(f"foo.x: {foo.x}")  # @x.getter

del foo.x  # @x.deleter

print(f"foo.x: {foo.x}")  # @x.getter
