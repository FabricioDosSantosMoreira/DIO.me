# - - - - -> Estruturas Condicionais:

    # As estruturas condicionais são blocos de código que permitem executar diferentes ações 
    # com base em condições específicas. Elas permitem que um programa tome decisões, 
    # avaliando se uma expressão é verdadeira ou falsa e executando diferentes 
    # trechos de código de acordo com o resultado dessa avaliação. 


# - - - - > Estruturas Condicionais Simples:
idade = 20

# - - -> Exemplo de Estrutura Condicional 'if':
print("\nExemplo de estrutura condicional 'if':")
if idade >= 18:
    print("Você é maior de idade.")


# - - -> Exemplo de Estrutura Condicional 'if' e 'else':
print("\nExemplo de estrutura condicional 'if' e 'else':")
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# - - -> Exemplo de Estrutura Condicional 'if', 'elif' e 'else':
print("\nExemplo de estrutura condicional 'if', 'elif' e 'else':")
if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é maior de idade.")


# Utilizando Operadores Lógicos (and, or, not) em Estruturas Condicionais:
print("\nUtilizando operadores lógicos (and, or, not) em estruturas condicionais:")
temperatura = 25
if idade >= 18 and temperatura > 20:
    print("Condições ideais para sair.")


# - - - -> Estruturas Condicionais Aninhadas:
possui_cartao = True
idade = 20

print("\nExemplo de estrutura condicional aninhada:")
if idade >= 18:
    print("Você é maior de idade.")
    
    if possui_cartao:
        print("Você pode fazer compras com desconto.")
    else:
        print("Você pode fazer compras, mas não terá desconto.")
else:
    print("Você é menor de idade.")


# - - - -> Estruturas Condicionais Ternária:

# - - -> Exemplo de Estrutura Condicional em uma linha (ternário):
resultado = "Aprovado" if idade >= 18 else "Reprovado"

print("\nExemplo de estrutura condicional em uma linha (ternário):")
print("Resultado:", resultado)