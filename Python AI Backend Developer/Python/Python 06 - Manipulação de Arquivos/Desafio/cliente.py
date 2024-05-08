from datetime import date


class Cliente():

    def __init__(self, endereco: str) -> None:

        self._endereco = endereco
        self._contas: list = []


    def realizar_transacao(self, transacao, conta) -> None:
        qtd_transacoes_hoje = conta.historico.transacoes_do_dia()

        if qtd_transacoes_hoje >= conta.limite_transacoes:
            print("\nERRO - - -> O número máximo de saques diários já foi atingido. Volte amanhã!")
            return

        transacao.registrar(conta)


    def adicionar_conta(self, conta) -> None:
        self._contas.append(conta)


    def __str__(self) -> str:
        return f"Nome: {self.nome}, Endereço: {self.endereco}"
    
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.cpf}')>"


    @property
    def endereco(self) -> str:
        return self._endereco
    
    @property
    def contas(self) -> list:
        return self._contas

 
class PessoaFisica(Cliente): # Extende a classe Cliente. Herança simples

    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: date) -> None:
        super().__init__(endereco=endereco)

        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento