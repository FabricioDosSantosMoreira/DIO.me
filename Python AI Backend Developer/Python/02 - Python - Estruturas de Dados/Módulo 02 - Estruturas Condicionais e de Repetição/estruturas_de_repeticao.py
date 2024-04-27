# São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. 
# Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.


# Exemplo de loop usando a estrutura 'for'
frutas = ["maçã", "banana", "laranja", "morango"]
print("\nExemplo de loop usando 'for':")
for fruta in frutas:
    print(fruta)

# A estrutura 'for' itera sobre cada elemento da lista 'frutas' e executa o bloco de código dentro do loop para cada elemento.


# Exemplo de loop usando a estrutura 'while'
contador = 0

print("\nExemplo de loop usando 'while':")
while contador < 5:
    print(contador)
    contador += 1

# A estrutura 'while' executa o bloco de código dentro do loop enquanto a condição especificada for verdadeira. 
# Aqui, o loop continua enquanto o valor de 'contador' for menor que 5.


# Exemplo utilizando else em uma estrutura de repetição
texto = "Hello World!"
VOGAIS = "AEIOU"

print("\nExemplo de loop usando 'for e else':")
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("\nTerminei de verificar as vogais") 

# Se executarmos esse código, a saída será "eoo", seguida pela mensagem "Terminei de verificar as vogais". 
# Isso ocorre porque as vogais 'e' e 'o' são encontradas no texto, e depois que o loop é concluído, 
# o bloco de código dentro do else é executado. 
# Se o loop for interrompido por um break, o bloco do else não será executado.