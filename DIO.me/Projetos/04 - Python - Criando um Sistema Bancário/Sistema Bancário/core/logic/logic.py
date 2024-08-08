from core.cliente import PessoaFisica
from core.conta import ContaCorrente, ContaIterador
from core.transacao import Saque, Deposito

from datetime import date, datetime

from util.utils import realizar_log, ler_int, ler_string
import pytz

from typing import Union, List


def escolher_conta_cliente(cliente: PessoaFisica) -> Union[ContaCorrente, None]:
    if not cliente.contas:  # O cliente não possui conta?
        print("\nERRO - - -> O cliente não possui contas registradas!")
        return

    if len(cliente.contas) == 1:  # O cliente possui uma conta?
        return cliente.contas[0]

    print()
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    print("|   Opções    |   Número da conta                               |")
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")

    for i, conta in enumerate(cliente.contas):
        espaco_opcoes = 8 - len(str(i + 1))

        print(f"|    [{i + 1}]" + "|".rjust(espaco_opcoes) + f"    {conta.numero}" + "|".rjust(46 - len(str(conta.numero))))
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")

    while True:
        try:
            opcao = ler_int("\n- - - - - - -> Informe a conta que deseja usar: ") - 1

            if opcao != -1:
                conta = cliente.contas[opcao]
                return conta
            raise IndexError
        except IndexError:
            print("\nERRO - - -> Opção de conta informada não existe!")


def existe_cliente(cpf: str, clientes: List[PessoaFisica]) -> Union[PessoaFisica, None]:

    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]

    return clientes_filtrados[0] if clientes_filtrados else None


def ler_e_verificar_cpf() -> Union[str, None]:
    cpf = ler_string("\n- - - - - - -> Informe o seu CPF: ")
    cpf_filtrado = ""

    for s in cpf:
        try:  # Filtra somente inteiros do cpf informado
            cpf_filtrado += f"{int(s)}"

        except Exception:
            pass

    if not len(cpf_filtrado) == 11:  # O cpf informado não tem 11 digitos?
        print("\nERRO - - -> O cpf informado é inválido!")
        return None

    return cpf_filtrado


@realizar_log
def criar_cliente(clientes: List) -> None:
    cpf = ler_e_verificar_cpf()
    if not cpf:  # O cpf é inválido?
        return

    if existe_cliente(cpf, clientes):  # Já existe um cliente com este mesmo cpf?
        print("\nERRO - - -> Já existe um cliente com este mesmo cpf!")
        return

    nome = ler_string("\n- - - - - - -> Informe o seu nome completo: ")
    endereco = ler_string("\n- - - - - - -> Informe o seu endereço: ")
    ano_nascimento = ler_int("\n- - - - - - -> Informe o seu ano de nascimento: ")
    mes_nascimento = ler_int("\n- - - - - - -> Informe o seu mês de nascimento: ")
    dia_nascimento = ler_int("\n- - - - - - -> Informe o seu dia de nascimento: ")

    data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)

    cliente = PessoaFisica(endereco=endereco, cpf=cpf, nome=nome, data_nascimento=data_nascimento)
    clientes.append(cliente)

    print("\nSUCESSO - - -> Cliente criado com sucesso!")

    return clientes


@realizar_log
def criar_conta(clientes: List, contas: List) -> None:
    cpf = ler_e_verificar_cpf()
    if not cpf:  # O cpf é inválido?
        return

    cliente = existe_cliente(cpf, clientes)
    if not cliente:  # Não existe um cliente com este cpf?
        print("\nERRO - - -> Não existe um cliente cadastrado com este cpf!")
        return

    numero_conta = len(contas) + 1

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nSUCESSO - - -> Conta criada com sucesso!")

    return clientes, contas


@realizar_log
def depositar(clientes: List) -> None:
    cpf = ler_e_verificar_cpf()
    if not cpf:  # O cpf é inválido?
        return

    cliente = existe_cliente(cpf, clientes)
    if not cliente:  # Não existe um cliente com este cpf?
        print("\nERRO - - -> O cliente não foi encontrado!")
        return

    conta = escolher_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("\n- - - - - - -> Informe o valor do depósito: "))
    if valor <= 0:
        print("\nERRO - - -> O valor do depósito deve ser positivo!")
        return

    transacao = Deposito(valor)
    cliente.realizar_transacao(transacao=transacao, conta=conta)

    return clientes


@realizar_log
def sacar(clientes: List) -> None:
    cpf = ler_e_verificar_cpf()
    if not cpf:  # O cpf é inválido?
        return

    cliente = existe_cliente(cpf, clientes)
    if not cliente:  # Não existe um cliente com este cpf?
        print("\nERRO - - -> O cliente não foi encontrado!")
        return

    conta = escolher_conta_cliente(cliente)
    if not conta:
        return

    valor = float(input("\n- - - - - - -> Informe o valor do saque: "))
    if valor <= 0:
        print("\nERRO - - -> O valor do depósito deve ser positivo!")
        return

    if valor > conta.limite:
        print(
            "\nERRO - - -> A sua conta não possui limite suficiente para realizar o saque!"
        )
        return

    transacao = Saque(valor)
    cliente.realizar_transacao(transacao=transacao, conta=conta)

    return clientes


@realizar_log
def exibir_extrato(clientes: List) -> None:
    cpf = ler_e_verificar_cpf()
    if not cpf:  # O cpf é inválido?
        return

    cliente = existe_cliente(cpf, clientes)
    if not cliente:  # Não existe um cliente com este cpf?
        print("\nERRO - - -> O cliente não foi encontrado!")
        return

    conta = escolher_conta_cliente(cliente)
    if not conta:
        return

    tipo_transacao = ler_string("\n - - -> Insira o tipo de transação (Saque/ Deposito/ Todos): ").lower()

    if tipo_transacao not in ["saque", "deposito", "todos"]:
        print("\nERRO - - -> O tipo de transação informado não é reconhecido!")
        return

    tipo_transacao = None if tipo_transacao == "todos" else tipo_transacao

    tem_transacao = False
    extrato = ""
    for transacao in conta.historico.gerar_relatorio(tipo_transacao):
        tem_transacao = True

        data_transacao = datetime.astimezone(transacao["data"], pytz.timezone("America/Sao_Paulo"))
        transacao_formatada = datetime.strftime(data_transacao, ("%Y/%m/%d %H:%M:%S"))

        extrato += f"|   {transacao["tipo"]}" + "|".rjust(11 - len(str(transacao["tipo"])))
        extrato += f"   {transacao["valor"]}" + "|".rjust(23 - len(str(transacao["valor"])))
        extrato += f"   {transacao_formatada}" + "|".rjust(21 - len(transacao_formatada))
        extrato += "\n"

    if not tem_transacao:
        print("\n- - -> Não houve nenhuma movimentação em sua conta bancária!")
        return

    saldo_formatado = f"{conta.saldo:.2f}"

    print()
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-+")
    print("|   Tipo      |    Valor da transação   |   Data                |")
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-+")
    print(extrato, end="")
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-+")
    print(f"|   Saldo: {saldo_formatado}" + "|".rjust(54 - len(saldo_formatado)))
    print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")

    return clientes


def listar_clientes(clientes: List) -> None:
    if len(clientes) == 0:
        print("\nNão há clientes para listar!")
        return

    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    print("|   Cliente   |   Informações do cliente                        |")
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    for i, cliente in enumerate(clientes):
        print(
            f"|   [{i}]"
            + "|".rjust(9 - len(str(i)))
            + f"   {cliente}"
            + "|".rjust(47 - len(str(cliente)))
        )
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")


def listar_contas(contas: List) -> None:
    if len(contas) == 0:
        print("\nNão há contas para listar!")
        return

    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    print("|   Conta     |    Informações da conta                                               |")
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    for i, conta in enumerate(ContaIterador(contas)):
        print(f"|   [{i}]" + "|".rjust(9 - len(str(i))) + f"   {conta}" + "|".rjust(69 - len(str(conta))))
    print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
