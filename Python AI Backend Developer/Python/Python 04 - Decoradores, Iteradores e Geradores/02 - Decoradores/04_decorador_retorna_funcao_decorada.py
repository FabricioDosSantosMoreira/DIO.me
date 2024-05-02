def meu_decorador(funcao):

    def envelope(*args, **kwargs):

        print("Faz algo antes de executar!")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar!")

        return resultado

    return envelope


@meu_decorador
def minha_função(argumento):
    print("Executando minha função!")
    return argumento.upper()


a = minha_função("arg")
print(a)