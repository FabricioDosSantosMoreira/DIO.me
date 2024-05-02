LIMITE_SAQUES = 3

numero_saques = 0
limite = 500
saldo = 0
extrato = ""


menu = """\n+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-+
|   Opções    |   Descrição     |
+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-+
|    [d]      |   Depositar     |
|    [s]      |   Sacar         |
|    [e]      |   Extrato       |
|    [q]      |   Sair          |
+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-+

- - -> Insira uma opção para continuar: """


while True:

    opcao = str(input(menu))

    match opcao.lower():

        case "d": # Depositar

            valor_deposito = float(input("\n- - -> Informe o valor do depósito: "))

            if not valor_deposito > 0: # O valor do depósito é positivo?
                print("\nERRO - - -> O valor do depósito deve ser positivo!")
                continue

            saldo += valor_deposito
            extrato += f"|  Depósito: R$ {valor_deposito:.2f}\n"

            print(f"\n- - -> Foi depositado R$ {valor_deposito:.2f} para a sua conta!")

            continue
        case "s": # Sacar

            if numero_saques >= LIMITE_SAQUES: # O número de saques atingiu o limite de saques?
                print("\nERRO - - -> O número máximo de saques diários já foi atingido. Volte amanhã!")
                continue

            valor_saque = float(input("\n- - -> Informe o valor do saque: "))

            if valor_saque > limite:
                print(f"\nERRO - - -> Impossível sacar um valor maior que o seu limite por saque. Limite por saque atual: R$ {limite:.2f}")
                continue

            if valor_saque > saldo:
                print(f"\nERRO - - -> Sem saldo disponível. Saldo atual: R$ {saldo:.2f}")
                continue

            saldo -= valor_saque
            numero_saques += 1
            extrato += f"|  Saque: R$ {valor_saque:.2f}\n"

            print(f"\n- - -> Foi sacado R$ {valor_saque:.2f} de sua conta!")

            continue
        case "e": # Extrato

            if not extrato:
                print("\nNão houve nenhuma movimentação em sua conta bancária!")
                continue
            
            print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
            print("|             EXTRATO               |")
            print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
            print(extrato)


            continue
        case "q": # Sair
            quit("\n- - -> Saindo do sistema bancário!")

        case _: # Default case
            print("\nERRO - - -> Operação inválida. Por favor, tente novamente.")