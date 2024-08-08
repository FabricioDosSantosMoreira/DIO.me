from core.logic.logic import *

class Interface(): 

    def __init__(self, app) -> None:
        from main import Main

        self.app: Main = app

        self.clientes: List = []
        self.contas: List = []
 

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


    def run(self) -> None:
        while True:

            opcao: int = self.menu()

            match opcao:
                case 1:
                    criar_cliente(self.clientes)

                    continue
                case 2:
                    criar_conta(self.clientes, self.contas)

                    continue
                case 3:
                    depositar(self.clientes)

                    continue
                case 4:
                    sacar(self.clientes)

                    continue
                case 5:
                    exibir_extrato(self.clientes)

                    continue
                case 6:
                    listar_clientes(self.clientes)

                    continue
                case 7:
                    listar_contas(self.contas)

                    continue
                case 8:
                    self.is_running = False
                    self.app.quit()
