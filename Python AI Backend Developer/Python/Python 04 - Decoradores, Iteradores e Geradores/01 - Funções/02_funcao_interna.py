def pricipal():
    print("Executando a função principal!")

    def funcao_interna():
        print("Executando a função interna!")

    def outra_funcao_interna():
        print("Executando a outra função interna!")


    funcao_interna()
    outra_funcao_interna()


pricipal()