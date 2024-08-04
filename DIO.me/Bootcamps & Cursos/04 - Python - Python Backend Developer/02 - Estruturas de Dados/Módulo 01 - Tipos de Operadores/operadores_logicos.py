# - - - - - > Operadores Lógicos:

#                 Os operadores lógicos são símbolos especiais usados para combinar ou manipular valores lógicos. 
#             Eles permitem criar expressões lógicas que ajudam a controlar o fluxo de um programa ou a 
#             tomar decisões com base em condições específicas.


# - - - - > Exemplos de Operadores Lógicos:
print("\nExemplos de Operadores Lógicos:")

# - - - > Operador lógico E (and):
print("\nOperador E (and):")

# NOTE: Retorna True, pois ambos os operandos são True
resultado = True and True
print(f"Resultado [True and True]: {resultado}")      

# NOTE: Retorna False, pois um dos operandos é False
resultado = True and False
print(f"Resultado [True and False]: {resultado}")   

# NOTE: Retorna False, pois um dos operandos é False
resultado = False and True
print(f"Resultado [False and True]: {resultado}")   

# NOTE: Retorna False, pois ambos os operandos são False
resultado = False and False
print(f"Resultado [False and False]: {resultado}")   

# NOTE: Retorna True, pois (True and True) é True e False é False
resultado = (True and True) or False
print(f"Resultado [(True and True) or False]: {resultado}")   

# NOTE: Retorna True, pois False or True é True e True é True
resultado = True and (False or True)
print(f"Resultado [True and (False or True)]: {resultado}")   


# - - - > Operador lógico OU (or):
print("\nOperador OU (or):")

# NOTE: Retorna True, pois um dos operandos é True
resultado = True or True
print(f"Resultado [True or True]: {resultado}")      

# NOTE: Retorna True, pois um dos operandos é True
resultado = True or False
print(f"Resultado [True or False]: {resultado}")   

# NOTE: Retorna True, pois um dos operandos é True
resultado = False or True
print(f"Resultado [False or True]: {resultado}")     

# NOTE: Retorna False, pois ambos os operandos são False
resultado = False or False
print(f"Resultado [False or False]: {resultado}")   

# NOTE: Retorna False, pois (True or True) é True e False é False
resultado = (True or True) and False
print(f"Resultado [(True or True) and False]: {resultado}")     

# NOTE: Retorna True, pois False and True é False e True é True
resultado =  True or (False and True)
print(f"Resultado [True or (False and True)]: {resultado}")   


# - - - > Operador lógico NÃO (not):
print(f"\nOperador NÃO (not):")

# NOTE: Retorna False, pois nega o valor True
resultado = not True
print(f"Resultado [not True]: {resultado}")   

# NOTE: Retorna True, pois nega o valor False
resultado = not False
print(f"Resultado [not False]: {resultado}")    

# NOTE: Retorna False, pois (True and True) é True, então not True é False
resultado = not (True and True)
print(f"Resultado [not (True and True)]: {resultado}")   

# NOTE: Retorna False, pois (False or True) é True, então not True é False
resultado = not (False or True)
print(f"Resultado [not (False or True)]: {resultado}")   


# - - - > Operadores lógicos combinados:
print("\nOperadores lógicos combinados:")

x: int = 5

# NOTE: Retorna True, pois x é maior que 0 e menor que 10
resultado = x > 0 and x < 10
print(f"Resultado [x > 0 and x < 10]: {resultado}")   

# NOTE: Retorna False, pois x não é menor que 0
resultado =  x < 0 or x % 2 == 0
print(f"Resultado [x < 0 or x % 2 == 0]: {resultado}")   

# NOTE: Retorna False, pois x é igual a 5
resultado = not(x == 5)
print(f"Resultado [not(x == 5)]: {resultado}")   

# NOTE: Retorna True, pois x é maior que 0 e (x < 10 or x == 5) é True
resultado = x > 0 and (x < 10 or x == 5)
print(f"Resultado [x > 0 and (x < 10 or x == 5)]: {resultado}")   

# NOTE: Retorna False, pois (x < 0 or x % 2 == 0) é False e not (x == 5) é False
resultado = (x < 0 or x % 2 == 0) and not(x == 5)
print(f"Resultado [(x < 0 or x % 2 == 0) and not(x == 5)]: {resultado}")   
