# - - - - - > Iteradores:
#                 Iteradores são objetos que permitem percorrer coleções de elementos de maneira sequencial.
#             Eles implementam o protocolo de iteração, o que significa que podem ser usados em estruturas
#             de controle como 'for' loops e também com funções que esperam iteradores como argumento.


# - - - - > Exemplo de Iteradores:
print("\nExemplo de Iteradores:")

from typing import List, Iterator

# - - - > Criando um Iterador:
class Iterador():

    def __init__(self, numeros: List[int]) -> None:
        self.numeros: List[int] = numeros
        self.contador: int = 0


    def __iter__(self) -> Iterator[int]:
        return self


    def __next__(self) -> int:
        try:
            numero: int = self.numeros[self.contador]
            self.contador += 1

            return numero * 2
        
        except IndexError:
            raise StopIteration


# - - - > Usando o Iterador:
print("\nUsando o Iterador:")

iterador: Iterador = Iterador(numeros=[10, 20, 30, 40, 50])

for n in iterador:
    print(f"Número: {n}")

for n in Iterador(numeros=[1, 2, 3, 4, 5]):
    print(f"Número: {n}")
    