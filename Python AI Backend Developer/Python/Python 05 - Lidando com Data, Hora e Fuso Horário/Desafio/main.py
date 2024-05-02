from transacao import Deposito, Saque
from cliente import PessoaFisica
from conta import ContaCorrente, ContaIterador

from datetime import date, datetime
from typing import Union, List
import pytz

class Main():

    def __init__(self) -> None:
        self.is_running = True

        self.clientes: List[PessoaFisica] = []
        self.contas: List[ContaCorrente] = []
        

    def menu(self) -> int:
        print()
        print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("|   Opções    |   Descrição                                     |")
        print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("|    [1]      |   Novo cliente                                  |")
        print("|    [2]      |   Nova conta                                    |")
        print("|    [3]      |   Depositar                                     |")
        print("|    [4]      |   Sacar                                         |")
        print("|    [5]      |   Exibir extrato                                |")
        print("|    [6]      |   Listar usuários                               |")
        print("|    [7]      |   Listar contas                                 |")
        print("|    [8]      |   Sair                                          |")
        print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        
        try:
            opcao = int(input("\n- - - - - - -> Insira uma opção para continuar: "))
            return opcao

        except ValueError:
            print("\nERRO- - -> Opção inválida. Por favor, tente novamente!")


    def run(self):
        while self.is_running:   

            opcao = self.menu()

            match opcao:

                case 1:
                    self.criar_cliente()

                    continue
                case 2:
                    self.criar_conta()

                    continue
                case 3:
                    self.depositar()

                    continue
                case 4:
                    self.sacar()

                    continue
                case 5:
                    self.exibir_extrato()
                    
                    continue
                case 6:
                    self.listar_clientes()

                    continue
                case 7:
                    self.listar_contas()

                    continue
                case 8: 
                    print("\nAVISO - - -> Saindo do sistema...")
                    self.is_running = False
                    quit()


    def log_transacao(func): # Decorador

        def envelope(*args, **kwargs):

            print(f"\n- - -> Data da transação: {datetime.now()}, Tipo da transação: {func.__name__.upper()}")
            func(*args, **kwargs)

        return envelope


    def escolher_conta_cliente(self, cliente: PessoaFisica) -> Union[ContaCorrente, None]:

        if not cliente.contas: # O cliente não possui conta?
            print("\nERRO - - -> O cliente não possui contas registradas!")
            return
        
        if len(cliente.contas) == 1: # O cliente possui uma conta?
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
                opcao = self.ler_int("\n- - - - - - -> Informe a conta que deseja usar: ") - 1

                if opcao != -1 :
                    conta = cliente.contas[opcao]
                    return conta
                
                raise IndexError

            except IndexError:
                print("\nERRO - - -> Opção de conta informada não existe!")


    def existe_cliente(self, cpf: str, clientes: List[PessoaFisica]) -> Union[PessoaFisica, None]:

        clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]

        return clientes_filtrados[0] if clientes_filtrados else None


    def ler_e_verificar_cpf(self) -> Union[str, None]:

        cpf = self.ler_string("\n- - - - - - -> Informe o seu CPF: ")

        cpf_filtrado = ""
        
        for s in cpf:
            try: # Filtra somente inteiros do cpf informado
                cpf_filtrado += f"{int(s)}"

            except Exception as e:
                pass

        if not len(cpf_filtrado) == 11: # O cpf informado não tem 11 digitos?
            print("\nERRO - - -> O cpf informado é inválido!")
            return None
        
        return cpf_filtrado


    def ler_string(self, msg: str) -> str:

        while True:
            try:
                str_input= str(input(msg))

                if not str_input or str_input.isspace():
                    raise ValueError
                
                return str_input

            except ValueError:
                print("\nERRO - - -> Input inválido. Por favor, tente novamente!")


    def ler_int(self, msg: str) -> int:

        while True:
            try:
                int_input= int(input(msg))    
                return int_input

            except ValueError:
                print("\nERRO - - -> Input inválido. Por favor, tente novamente!")


    @log_transacao
    def criar_cliente(self) -> None:

        cpf = self.ler_e_verificar_cpf()
        if not cpf: # O cpf é inválido?
            return
        
        if self.existe_cliente(cpf, self.clientes): # Já existe um cliente com este mesmo cpf?
            print("\nERRO - - -> Já existe um cliente com este mesmo cpf!")
            return
        

        nome = self.ler_string("\n- - - - - - -> Informe o seu nome completo: ")
        endereco = self.ler_string("\n- - - - - - -> Informe o seu endereço: ")
        ano_nascimento = self.ler_int("\n- - - - - - -> Informe o seu ano de nascimento: ")
        mes_nascimento = self.ler_int("\n- - - - - - -> Informe o seu mês de nascimento: ")
        dia_nascimento = self.ler_int("\n- - - - - - -> Informe o seu dia de nascimento: ")
        
        data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)


        cliente = PessoaFisica(endereco=endereco, cpf=cpf, nome=nome, data_nascimento=data_nascimento)
        self.clientes.append(cliente)

        print("\nSUCESSO - - -> Cliente criado com sucesso!")


    @log_transacao
    def criar_conta(self) -> None:

        cpf = self.ler_e_verificar_cpf()
        if not cpf: # O cpf é inválido?
            return
        
        cliente = self.existe_cliente(cpf, self.clientes)
        if not cliente: # Não existe um cliente com este cpf?
            print("\nERRO - - -> Não existe um cliente cadastrado com este cpf!")
            return 
    
        numero_conta = len(self.contas) + 1


        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        self.contas.append(conta)
        cliente.contas.append(conta)

        print("\nSUCESSO - - -> Conta criada com sucesso!")

        
    @log_transacao
    def depositar(self) -> None:
        
        cpf = self.ler_e_verificar_cpf()
        if not cpf: # O cpf é inválido?
            return
        
        cliente = self.existe_cliente(cpf, self.clientes)
        if not cliente: # Não existe um cliente com este cpf?
            print("\nERRO - - -> O cliente não foi encontrado!")
            return 

        conta = self.escolher_conta_cliente(cliente)
        if not conta:
            return


        valor = float(input("\n- - - - - - -> Informe o valor do depósito: "))
        if valor <= 0:
            print("\nERRO - - -> O valor do depósito deve ser positivo!")
            return

        transacao = Deposito(valor)
        cliente.realizar_transacao(transacao=transacao, conta=conta)


    @log_transacao 
    def sacar(self) -> None:

        cpf = self.ler_e_verificar_cpf()
        if not cpf: # O cpf é inválido?
            return
        
        cliente = self.existe_cliente(cpf, self.clientes)
        if not cliente: # Não existe um cliente com este cpf?
            print("\nERRO - - -> O cliente não foi encontrado!")
            return 

        conta = self.escolher_conta_cliente(cliente)
        if not conta:
            return


        valor = float(input("\n- - - - - - -> Informe o valor do saque: "))
        if valor <= 0:
            print("\nERRO - - -> O valor do depósito deve ser positivo!")
            return
        
        if valor > conta.limite:
            print("\nERRO - - -> A sua conta não possui limite suficiente para realizar o saque!")
            return

        transacao = Saque(valor)
        cliente.realizar_transacao(transacao=transacao, conta=conta)


    @log_transacao 
    def exibir_extrato(self) -> None:

        cpf = self.ler_e_verificar_cpf()
        if not cpf: # O cpf é inválido?
            return
        
        cliente = self.existe_cliente(cpf, self.clientes)
        if not cliente: # Não existe um cliente com este cpf?
            print("\nERRO - - -> O cliente não foi encontrado!")
            return 

        conta = self.escolher_conta_cliente(cliente)
        if not conta:
            return
        
        tipo_transacao = self.ler_string("\n - - -> Insira o tipo de transação (Saque/ Deposito/ Todos): ").lower()

        if not tipo_transacao in ["saque", "deposito", "todos"]:
            print("\nERRO - - -> O tipo de transação informado não é reconhecido!")
            return

        tipo_transacao = None if tipo_transacao == "todos" else tipo_transacao

        tem_transacao = False
        extrato = ""
        for transacao in conta.historico.gerar_relatorio(tipo_transacao):
            tem_transacao = True

            data_transacao = datetime.astimezone(transacao['data'], pytz.timezone('America/Sao_Paulo'))
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


    def listar_clientes(self) -> None:
        if len(self.clientes) == 0:
            print("\nNão há cliente para listar!")
            return
        
        print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("|   Cliente   |   Informações do cliente                        |")
        print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        for i, cliente in enumerate(self.clientes):
            print(f"|   [{i}]" + "|".rjust(9 - len(str(i))) + f"   {cliente}" + "|".rjust(47 - len(str(cliente))))
        print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")


    def listar_contas(self) -> None:

        if len(self.contas) == 0:
            print("\nNão há contas para listar!")
            return
        
        print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("|   Conta     |    Informações da conta                                               |")
        print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        for i, conta in enumerate(ContaIterador(self.contas)):
            print(f"|   [{i}]" + "|".rjust(9 - len(str(i))) + f"   {conta}" + "|".rjust(69 - len(str(conta))))
        print("+-=-=-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")


if __name__ == "__main__":
    app = Main() 
    app.run()