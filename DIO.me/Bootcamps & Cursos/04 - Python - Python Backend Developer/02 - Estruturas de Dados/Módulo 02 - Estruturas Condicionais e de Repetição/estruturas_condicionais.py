# - - - - - > Estruturas Condicionais:

#                 As estruturas condicionais são blocos de código que permitem executar diferentes ações 
#            com base em condições específicas. Elas permitem que um programa tome decisões, 
#            avaliando se uma expressão é verdadeira ou falsa e executando diferentes 
#            trechos de código de acordo com o resultado dessa avaliação. 


# - - - - > Exemplos de Estruturas Condicionais Simples:
print("\nExemplos de Estruturas Condicionais Simples:")

idade: int = 20

# - - - > Exemplo de Estrutura Condicional 'if':
print("\nExemplo de Estrutura Condicional 'if':")
if idade >= 18:
    print("Você é maior de idade.")


# - - - > Exemplo de Estrutura Condicional 'if' e 'else':
print("\nExemplo de Estrutura Condicional 'if' e 'else':")
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# - - - > Exemplo de Estrutura Condicional 'if', 'elif' e 'else':
print("\nExemplo de Estrutura Condicional 'if', 'elif' e 'else':")
if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é maior de idade.")


# Utilizando operadores lógicos em estruturas condicionais:
print("\nUtilizando operadores lógicos em estruturas condicionais:")
temperatura = 25
if idade >= 18 and temperatura > 20:
    print("Condições ideais para sair.")


# - - - - > Exemplo de Estrutura Condicional Aninhada:
possui_cartao: bool = True
idade: int = 20

print("\nExemplo de Estrutura Condicional Aninhada:")
if idade >= 18:
    print("Você é maior de idade.")

    if possui_cartao:
        print("Você pode fazer compras com desconto.")
    else:
        print("Você pode fazer compras, mas não terá desconto.")
else:
    print("Você é menor de idade.")


# - - - -> Exemplo de Estrutura Condicional Ternária (em uma linha):

resultado = "Aprovado" if idade >= 18 else "Reprovado"

print("\nExemplo de Estrutura Condicional Ternária (em uma linha):")
print(f"Resultado: {resultado}")
