# - - - - - > Estruturas de Repetição:

#                 São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. 
#             Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.


# - - - - > Exemplos de Estruturas de Repetição 'for':
print("\nExemplos de Estruturas de Repetição 'for':")

# - - - > Exemplo de Estrutura de Repetição 'for' simples:
frutas: list = ["maçã", "banana", "laranja", "morango"]

print("\nExemplo de Estrutura de Repetição 'for' Simples:")
for fruta in frutas:
    print(fruta)

#   NOTE: A estrutura 'for' itera sobre cada elemento da lista 'frutas' e 
#   executa o bloco de código dentro do loop para cada elemento.


# - - - > Exemplo de Estrutura de Repetição 'for' Aninhado:
print("\nExemplo de Estrutura de Repetição 'for' Aninhado:")
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)


# - - - - > Exemplos de Estruturas de Repetição 'while':
print("\nExemplos de Estruturas de Repetição 'while':")

# - - - > Exemplo de Estrutura de Repetição 'while' Simples:
contador: int = 0

print("\nExemplo de Estrutura de Repetição 'while' Simples:")
while contador < 5:
    print(f"contador = {contador}")
    contador += 1

#   NOTE: A estrutura 'while' executa o bloco de código dentro do loop enquanto 
#   a condição especificada for verdadeira. Aqui, o loop continua enquanto o 
#   valor de 'contador' for menor que 5.


# - - - > Exemplo de Estrutura de Repetição 'while' Aninhada:
linha: int = 0
coluna: int = 0

print("\nExemplo de Estrutura de Repetição 'while' Aninhada:")
while linha < 5:
    while coluna < 5:
        print(f"linha = {linha}, coluna = {coluna}")
        coluna += 1
    linha += 1
    coluna = 0


# - - - - > Outros Casos:
print("\nOutros Casos:")

# - - - > Exemplo Utilizando 'else' em uma Estrutura de Repetição 'for': 
texto: str = "Hello World!"
VOGAIS: str = "AEIOU"

print("\nExemplo Utilizando 'else' em uma Estrutura de Repetição 'for':")
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("\nTerminei de verificar as vogais!") 

#   NOTE: Se executarmos esse código, a saída será "eoo", seguida pela mensagem "Terminei de verificar as vogais". 
#   Isso ocorre porque as vogais 'e' e 'o' são encontradas no texto, e depois que o loop é concluído, 
#   o bloco de código dentro do else é executado. 

#   NOTE: Se o loop for interrompido por um break, o bloco do else não será executado.
    