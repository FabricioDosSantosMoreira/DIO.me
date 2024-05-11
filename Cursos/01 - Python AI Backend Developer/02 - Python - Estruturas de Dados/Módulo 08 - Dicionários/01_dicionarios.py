# - - - - -> Dicionários: Criação, Acesso e Modificação

# Dicionários são estruturas de dados em Python que armazenam pares chave-valor.
# Eles são úteis para mapear um conjunto de chaves a um conjunto de valores correspondentes.

# - - -> Criação de um dicionário:
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
print("\nDicionário criado:", meu_dicionario)

# - - -> Acesso aos valores de um dicionário:
print("\nAcesso aos valores do dicionário:")
print("Nome:", meu_dicionario['nome'])
print("Idade:", meu_dicionario['idade'])
print("Cidade:", meu_dicionario['cidade'])

# - - -> Modificação de valores em um dicionário:
print("\nModificação de valores no dicionário:")
meu_dicionario['idade'] = 35
print("Idade atualizada:", meu_dicionario['idade'])

# - - -> Adição de novos pares chave-valor em um dicionário:
print("\nAdição de novo par chave-valor:")
meu_dicionario['profissao'] = 'Engenheiro'
print("Dicionário atualizado:", meu_dicionario)

# - - -> Remoção de um par chave-valor de um dicionário:
print("\nRemoção de um par chave-valor:")
del meu_dicionario['cidade']
print("Dicionário após remoção:", meu_dicionario)
