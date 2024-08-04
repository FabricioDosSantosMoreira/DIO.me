# - - - - - > Funções de Entrada e Saída:

# - - - - > Funções de Entrada:
#               Funções de entrada são utilizadas quando queremos ler dados da entrada 
#           padrão. No python a função builtin 'input()' é uma função de entrada. Ela 
#           recebe um argumento do tipo string, que é exibido para o usuário na 
#           saída padrão. A função lê a entrada, converte para string e retorna 
#           o valor.


# - - - - > Funções de Saída:
#               Funções de saída são utilizadas quando queremos exibir dados na saída 
#           padrão. No python a função builtin 'print()' é uma função de saída. Ela 
#           recebe um argumento obrigatório do tipo varargs de objetos e outros 
#           4 argumentos opcionais 'sep', 'end', 'file' e 'flush'. Todos os 
#           objetos são convertidos para string exibidos para o usuário.


# - - - - > Exemplo de Funções de Entrada e Saída:
print("\nExemplo de Funções de Entrada e Saída:")

# - - - > Exemplo de Função de Entrada 'input()':
print("\nExemplo de Função de Entrada 'input()':")

nome = input("\nInforme o seu nome: ")
idade = input("\nInforme a sua idade: ")


# - - - > Exemplo de Função de Saída 'print()':
print("\nExemplo de Função de Saída 'print()':")

print()
print(nome, idade)
print(nome, idade, sep="-")
print(nome, idade, end=".\n")
print(nome, idade, sep="-", end=".\n")
