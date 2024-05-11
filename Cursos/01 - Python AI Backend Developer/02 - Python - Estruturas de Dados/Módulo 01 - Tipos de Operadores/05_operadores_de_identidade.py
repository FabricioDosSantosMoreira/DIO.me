# - - - - -> Operadores de Identidade:

    # Os operadores de identidade, is e is not, são utilizados para verificar 
    # se duas variáveis estão se referindo ao mesmo objeto na memória.


x = 5
y = 5
z = [1, 2, 3]
w = [1, 2, 3]

# - - - -> Operador de Identidade is:
# OBS: retorna True se as duas variáveis apontarem para o mesmo objeto na memória

print("\nOperador de identidade 'is':")
print("x is y:", x is y)  # x e y apontam para o mesmo objeto (5) na memória, então retorna True
print("z is w:", z is w)  # z e w são listas diferentes, mesmo que contenham os mesmos elementos, então retorna False


# - - - -> Operador de Identidade is not:
# OBS: retorna True se as duas variáveis não apontarem para o mesmo objeto na memória

print("\nOperador de identidade 'is not':")
print("x is not y:", x is not y)  # x e y apontam para o mesmo objeto (5) na memória, então retorna False
print("z is not w:", z is not w)  # z e w são listas diferentes, mesmo que contenham os mesmos elementos, então retorna True


# Alterando w para que aponte para o mesmo objeto que z
w = z
print("\nDepois de alterar w para apontar para o mesmo objeto que z:")
print("z is w:", z is w)  # Agora z e w apontam para o mesmo objeto, então retorna True
