# - - - - -> Métodos da Classe list:

    # Os métodos da classe list são funções incorporadas que podem ser usadas para modificar e 
    # manipular listas em Python.


# - - - -> Método: append()
lista = [1, 2, 3]
lista.append(4)
print("\nMétodo append():", lista)

# - - - -> Método: extend()
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print("\nMétodo extend():", lista1)

# - - - -> Método: insert()
lista = [1, 2, 3]
lista.insert(1, 5)
print("\nMétodo insert():", lista)

# - - - -> Método: remove()
lista = [1, 2, 3, 4, 3]
lista.remove(3)
print("\nMétodo remove():", lista)

# - - - -> Método: pop()
lista = [1, 2, 3]
elemento_removido = lista.pop()
print("\nMétodo pop() - Elemento removido:", elemento_removido)
print("Lista após pop():", lista)

# - - - -> Método: clear()
lista = [1, 2, 3]
lista.clear()
print("\nMétodo clear() - Lista após clear():", lista)

# - - - -> Método: index()
lista = [1, 2, 3, 4]
indice = lista.index(3)
print("\nMétodo index() - Índice do elemento 3:", indice)

# - - - -> Método: count()
lista = [1, 2, 3, 3, 4, 3]
ocorrencias = lista.count(3)
print("\nMétodo count() - Número de ocorrências do elemento 3:", ocorrencias)

# - - - -> Método: sort()
lista = [3, 2, 1, 4]
lista.sort()
print("\nMétodo sort() - Lista ordenada:", lista)

# - - - -> Método: reverse()
lista = [1, 2, 3, 4]
lista.reverse()
print("\nMétodo reverse() - Lista invertida:", lista)

# - - - -> Método: copy()
lista = [1, 2, 3]
copia_lista = lista.copy()
print("\nMétodo copy() - Cópia da lista:", copia_lista)

# - - - -> Método: join() (não é um método da classe list, mas é comumente usado com listas)
lista = ['Hello', 'world']
texto = ' '.join(lista)
print("\nMétodo join() - Texto concatenado:", texto)
