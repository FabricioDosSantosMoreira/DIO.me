# - - - - -> Funções de Entrada e Saída:

# - - -> input():
# A função builtin 'input' do python é utilizada quando queremos ler dados da entrada padrão. 
# Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão. 
# A função lê a entrada, converte para string e retorna o valor.

# - - -> print():
# A função builtin 'print' do python é utilizada quando queremos exibir dados na saída padrão. 
# Ela recebe um argumento obrigatório do tipo varargs de objetos e outros 4 argumentos 
# opcionais (sep, end, file e flush). Todos os objetos são convertidos para string. 
# A string final é exibida para o usuário.


nome = input("\nInforme o seu nome: ")

idade = input("\nInforme a sua idade: ")


print()

print(nome, idade)

print(nome, idade, sep="-")

print(nome, idade, end=".\n")

print(nome, idade, sep="-", end=".\n")