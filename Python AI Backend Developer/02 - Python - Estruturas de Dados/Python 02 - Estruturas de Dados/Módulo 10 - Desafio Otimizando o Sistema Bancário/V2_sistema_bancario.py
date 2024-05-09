def menu() -> None:
    menu = """\n
    +-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+
    |   Opções    |   Descrição                                     |
    +-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+
    |    [1]      |   Depositar                                     |
    |    [2]      |   Sacar                                         |
    |    [3]      |   Exibir extrato e saldo                        |
    |    [4]      |   Novo usuário                                  |
    |    [5]      |   Nova conta                                    |
    |    [6]      |   Listar contas                                 |
    |    [7]      |   Sair                                          |
    +-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+
    
    \n- - - - - - -> Insira uma opção para continuar: """

    return str(input(menu))


def depositar(saldo: float, valor: float, extrato: list, /) -> tuple[float, str]:

    if not valor > 0: # O valor do depósito não é positivo?
        print("\nERRO - - -> O valor do depósito deve ser positivo!")
        
    else:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")

        print(f"\n- - -> Foi depositado R$ {valor:.2f} para a sua conta!")  


    return saldo, extrato


def sacar(*, saldo: float, valor: float, extrato: list, numero_saques: int, limite: float, limite_saques: int) -> tuple[float, str, int]:

    if numero_saques >= limite_saques: # O número de saques atingiu o limite de saques?
        print("\nERRO - - -> O número máximo de saques diários já foi atingido. Volte amanhã!")
        return saldo, extrato, numero_saques
    if valor > limite: # O valor do saque é maior que o limite?
        print(f"\nERRO - - -> Impossível sacar um valor maior que o seu limite. Limite atual: R$ {limite:.2f}")
        return saldo, extrato, numero_saques
    if valor > saldo: # O valor do saque é maior que o saldo disponível?
        print(f"\nERRO - - -> Sem saldo disponível. Saldo atual: R$ {saldo:.2f}")
        return saldo, extrato, numero_saques
    if valor > 0:
        
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque: R$ {valor:.2f}")

        print(f"\n- - -> Foi sacado R$ {valor:.2f} de sua conta!")
        return saldo, extrato, numero_saques
    else:
        print("\nERRO - - -> O valor do saque deve ser positivo!")
        return saldo, extrato, numero_saques


def exibir_extrato(saldo: float, /, *, extrato: list) -> None:
    if not extrato:
        print("\nNão houve nenhuma movimentação em sua conta bancária!")
        return
                    
    saldo_formatado = f"{saldo:.2f}"


    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")

    for i, ext in enumerate(extrato):
        print(f"|   [{i}]" + "|".rjust(9 - len(str(i))) + f"   {ext}")

    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    print(f"|   Saldo: R$ {saldo_formatado}" + "|".rjust(51 - len(saldo_formatado)))
    print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")


def criar_usuario(usuarios: list):

    cpf = input("\n- - -> Informe o seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n- - -> ERRO. Já existe um usuário com esse CPF!")
        return

    nome = input("\n- - -> Informe o seu nome completo: ")
    data_nascimento = input("\n- - ->Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("\n- - -> Informe o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário criado com sucesso!")


def filtrar_usuario(cpf: str, usuarios: list):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("\n- - -> Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")

        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nERRO - - -> Usuário não encontrado, criação de conta encerrado!")


def listar_contas(contas: list) -> None:

    if len(contas) == 0:
        print("\nNão há contas para listar!")
        return
    
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    for i, conta in enumerate(contas):
        print(f"|   [{i}]" + "|".rjust(9 - len(str(i))) + f"   {conta}")
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")


def main() -> None:
    LIMITE_SAQUES = 3 
    AGENCIA = "0001"

    numero_saques = 0
    limite = 500
    saldo = 0
    extrato = []

    usuarios = []
    contas = []
    
    while True:

        opcao = menu()

        match opcao:

            case "1": # Depositar

                valor = float(input("\n- - -> Informe o valor do depósito: "))

                saldo, extrato = depositar(saldo, valor, extrato)

                continue
            case "2": # Sacar

                valor = float(input("\n- - -> Informe o valor do saque: "))

                saldo, extrato, numero_saques = sacar(saldo=saldo,
                                       valor=valor,
                                       extrato=extrato,
                                       numero_saques=numero_saques,
                                       limite=limite,
                                       limite_saques=LIMITE_SAQUES)
                
                continue

            case "3": # Exibir extrato
                exibir_extrato(saldo, extrato=extrato)

                continue
            case "4": # Novo usuário
                criar_usuario(usuarios)

                continue
            case "5": # Nova conta
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                
                if conta:
                    contas.append(conta)

                continue
            case "6": # Listar contas
                listar_contas(contas)

                continue
            case "7": # Sair
                quit("\n- - -> Saindo do sistema bancário!")

            case _: # Default case
                print("\nERRO - - -> Operação inválida. Por favor, tente novamente.")


main()