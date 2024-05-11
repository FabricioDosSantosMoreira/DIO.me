# - - - - -> Operadores Lógicos:

    # Os operadores lógicos são símbolos especiais usados para combinar ou manipular valores lógicos. 
    # Eles permitem criar expressões lógicas que ajudam a controlar o fluxo de um programa ou a 
    # tomar decisões com base em condições específicas.


# - - - -> Operador Lógico E (and):
print("\nOperador E (and):")
print("True and True:", True and True)      # Retorna True, pois ambos os operandos são True
print("True and False:", True and False)    # Retorna False, pois um dos operandos é False
print("False and True:", False and True)    # Retorna False, pois um dos operandos é False
print("False and False:", False and False)  # Retorna False, pois ambos os operandos são False
print("(True and True) or False:", (True and True) or False)  # Retorna True, pois (True and True) é True e False é False
print("True and (False or True):", True and (False or True))  # Retorna True, pois False or True é True e True é True
print()


# - - - -> Operador Lógico OU (or):
print("\nOperador OU (or):")
print("True or True:", True or True)      # Retorna True, pois um dos operandos é True
print("True or False:", True or False)    # Retorna True, pois um dos operandos é True
print("False or True:", False or True)    # Retorna True, pois um dos operandos é True
print("False or False:", False or False)  # Retorna False, pois ambos os operandos são False
print("(True or True) and False:", (True or True) and False)  # Retorna False, pois (True or True) é True e False é False
print("True or (False and True):", True or (False and True))  # Retorna True, pois False and True é False e True é True
print()


# - - - -> Operador Lógico NÃO (not):
print("\nOperador NÃO (not):")
print("not True:", not True)    # Retorna False, pois nega o valor True
print("not False:", not False)  # Retorna True, pois nega o valor False
print("not (True and True):", not (True and True))  # Retorna False, pois (True and True) é True, então not True é False
print("not (False or True):", not (False or True))  # Retorna False, pois (False or True) é True, então not True é False
print()


# - - - -> Exemplos Combinados:
x = 5
print("\nExemplos combinados:")

# Retorna True, pois x é maior que 0 e menor que 10
print("x > 0 and x < 10:", x > 0 and x < 10)  

# Retorna False, pois x não é menor que 0
print("x < 0 or x % 2 == 0:", x < 0 or x % 2 == 0) 

# Retorna False, pois x é igual a 5
print("not(x == 5):", not (x == 5)) 

# Retorna True, pois x é maior que 0 e (x < 10 or x == 5) é True
print("x > 0 and (x < 10 or x == 5):", x > 0 and (x < 10 or x == 5)) 

# Retorna False, pois (x < 0 or x % 2 == 0) é False e not (x == 5) é False
print("(x < 0 or x % 2 == 0) and not (x == 5):", (x < 0 or x % 2 == 0) and not (x == 5))  
