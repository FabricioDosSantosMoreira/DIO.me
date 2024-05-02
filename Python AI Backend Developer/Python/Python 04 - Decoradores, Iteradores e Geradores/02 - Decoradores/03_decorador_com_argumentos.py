def meu_decorador(funcao):

    def envelope(*args, **kwargs):

        print("Faz algo antes de executar!")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar!")

    return envelope


@meu_decorador
def minha_função(argumento):
    print("Executando minha função!")
    print("Argumento: ", argumento)



minha_função("arg")