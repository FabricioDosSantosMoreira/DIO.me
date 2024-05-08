# As estruturas condicionais são blocos de código que permitem executar diferentes ações com base em condições específicas. 
# Elas permitem que um programa tome decisões, avaliando se uma expressão é verdadeira ou falsa e 
# executando diferentes trechos de código de acordo com o resultado dessa avaliação. 


# Definindo uma variável para testar
idade = 20
possui_cartao = True


# ---> Estruturas comndicionais simples

# Exemplo de estrutura condicional 'if'
if idade >= 18:
    print("Você é maior de idade.")


# Exemplo de estrutura condicional 'if' e 'else'
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# Exemplo de estrutura condicional 'if', 'elif' e 'else'
if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é maior de idade.")


# Utilizando operadores lógicos (and, or, not) em estruturas condicionais
temperatura = 25
if idade >= 18 and temperatura > 20:
    print("Condições ideais para sair.")


# ---> Estruturas condicionais aninhadas

# Verifica se a pessoa é maior de 18 anos
if idade >= 18:
    print("Você é maior de idade.")
    
    # Verifica se a pessoa possui um cartão
    if possui_cartao:
        print("Você pode fazer compras com desconto.")
    else:
        print("Você pode fazer compras, mas não terá desconto.")
else:
    print("Você é menor de idade.")


# ---> Estruturas condicionais ternária

# Estrutura condicional em uma linha (ternário)
resultado = "Aprovado" if idade >= 18 else "Reprovado"
print("Resultado:", resultado)