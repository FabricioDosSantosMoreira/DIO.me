# - - - - -> Estruturas de Repetição:

    # São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. 
    # Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.


# - - - -> Estrutura de Repetição 'for':

# - - -> Exemplo de Estrutura de Repetição 'for' simples:
frutas = ["maçã", "banana", "laranja", "morango"]

print("\nExemplo de estrutura de Repetição 'for' simples:")
for fruta in frutas:
    print(fruta)

    # OBS: A estrutura 'for' itera sobre cada elemento da lista 'frutas' e 
    # executa o bloco de código dentro do loop para cada elemento.


# - - -> Exemplo de Estrutura de Repetição 'for' aninhado:
print("\nExemplo de estrutura de Repetição 'for' aninhado:")
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)


# - - - -> Estrutura de Repetição 'while':

# - - -> Exemplo de Estrutura de Repetição 'while' simples:
contador = 0

print("\nExemplo de estrutura de Repetição 'while' simples:")
while contador < 5:
    print(f"contador = {contador}")
    contador += 1

    # OBS: A estrutura 'while' executa o bloco de código dentro do loop enquanto 
    # a condição especificada for verdadeira. Aqui, o loop continua enquanto o 
    # valor de 'contador' for menor que 5.

# - - -> Exemplo de Estrutura de Repetição 'while' aninhada:
linha = 0
coluna = 0

print("\nExemplo de estrutura de Repetição 'while' aninhada:")
while linha < 5:
    while coluna < 5:
        print(f"linha = {linha}, coluna = {coluna}")
        coluna += 1
    linha += 1
    coluna = 0


# - - - -> Outros Casos:

# - - -> Exemplo utilizando 'else' em uma Estrutura de Repetição 'for': 
texto = "Hello World!"
VOGAIS = "AEIOU"

print("\nExemplo utilizando 'else' em uma estrutura de repetição 'for':")
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("Terminei de verificar as vogais") 

    # OBS: Se executarmos esse código, a saída será "eoo", seguida pela mensagem "Terminei de verificar as vogais". 
    #   Isso ocorre porque as vogais 'e' e 'o' são encontradas no texto, e depois que o loop é concluído, 
    #   o bloco de código dentro do else é executado. 

    # OBS: Se o loop for interrompido por um break, o bloco do else não será executado.