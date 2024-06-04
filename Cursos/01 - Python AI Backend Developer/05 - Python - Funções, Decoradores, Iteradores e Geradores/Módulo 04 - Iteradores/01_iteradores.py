# - - - - -> Iteradores:

    #   Iteradores são objetos que permitem percorrer coleções de elementos de maneira sequencial.
    # Eles implementam o protocolo de iteração, o que significa que podem ser usados em estruturas
    # de controle como 'for' loops e também com funções que esperam iteradores como argumento.


# - - - - -> Exemplo de Iteradores:
class MeuIterador():
    def __init__(self, numeros: list[int]) -> None:
        self.numeros = numeros
        self.contador = 0


    def __iter__(self):
        return self


    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        
        except IndexError:
            raise StopIteration


# - - - -> Utilizando o Iterador:

meu_iterador = MeuIterador(numeros=[38, 13, 11, 25, 67])
print("\nUtilizando o Iterador:")
for numero in meu_iterador:
    print(f"\t{numero}")
