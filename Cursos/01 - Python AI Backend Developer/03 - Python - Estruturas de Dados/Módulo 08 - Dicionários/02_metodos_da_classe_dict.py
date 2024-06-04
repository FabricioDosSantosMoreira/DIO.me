# - - - - -> Métodos da Classe Dicionários:

# Os dicionários em Python são estruturas de dados poderosas que mapeiam chaves a valores.
# Existem diversos métodos úteis disponíveis para manipular dicionários em Python.

# - - -> Método: keys()
dicionario = {'a': 1, 'b': 2, 'c': 3}
chaves = dicionario.keys()
print("\nMétodo keys() - Chaves do dicionário:", chaves)

# - - -> Método: values()
valores = dicionario.values()
print("\nMétodo values() - Valores do dicionário:", valores)

# - - -> Método: items()
itens = dicionario.items()
print("\nMétodo items() - Pares chave-valor do dicionário:", itens)

# - - -> Método: get()
valor = dicionario.get('a')
print("\nMétodo get() - Valor associado à chave 'a':", valor)

# - - -> Método: pop()
valor_removido = dicionario.pop('b')
print("\nMétodo pop() - Valor removido associado à chave 'b':", valor_removido)
print("Dicionário após a remoção:", dicionario)

# - - -> Método: popitem()
par_removido = dicionario.popitem()
print("\nMétodo popitem() - Par chave-valor removido:", par_removido)
print("Dicionário após a remoção:", dicionario)

# - - -> Método: clear()
dicionario.clear()
print("\nMétodo clear() - Dicionário após limpeza:", dicionario)

# - - -> Método: update()
dicionario1 = {'a': 1, 'b': 2}
dicionario2 = {'b': 3, 'c': 4}
dicionario1.update(dicionario2)
print("\nMétodo update() - Dicionário atualizado:", dicionario1)

# - - -> Método: copy()
copia_dicionario = dicionario1.copy()
print("\nMétodo copy() - Cópia do dicionário:", copia_dicionario)

