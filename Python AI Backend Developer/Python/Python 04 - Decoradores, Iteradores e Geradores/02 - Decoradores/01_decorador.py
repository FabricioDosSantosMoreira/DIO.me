def meu_decorador(funcao):

    def envelope():
        print("Faz algo antes de executar!")
        funcao()
        print("Faz algo depois de executar!")

    return envelope


def minha_função():
    print("Executando minha função!")


minha_função = meu_decorador(minha_função)
minha_função()


