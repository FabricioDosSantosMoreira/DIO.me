from core.cliente import Cliente
from core.historico import Historico


class Conta:

    def __init__(self, cliente, numero: int) -> None:

        self._historico = Historico()
        self._cliente = cliente

        self._numero = numero
        self._saldo: float = 0.0
        self._agencia: str = "0001"
        self._numero_transacoes = 0


    @classmethod
    def nova_conta(cls, cliente, numero: int) -> "Conta":
        return cls(cliente, numero)


    def sacar(self, valor: float) -> bool:

        if valor > self.saldo:  # O valor de saque excedeu o saldo?
            print("\nERRO - - -> A operação falhou. Você não possui saldo suficiente!")
            return False

        elif valor <= 0:  # O valor de saque é inválido?
            print("\nERRO - - -> A operação falhou. O valor informado é inválido!")
            return False

        self._saldo -= valor
        print(f"\nSUCESSO - - -> Saque de R$ {valor:.2f} realizado com sucesso!")

        self._numero_transacoes += 1
        return True


    def depositar(self, valor: float) -> bool:

        if valor <= 0:  # O valor de depósito é invalido?
            print("\nERRO - - -> A operação falhou. O valor informado é inválido!")
            return False

        self._saldo += valor
        print(f"\nSUCESSO - - -> Depósito de R$ {valor:.2f} realizado com sucesso!")

        self._numero_transacoes += 1
        return True


    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> "Cliente":
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    @property
    def numero_transacoes(self) -> int:
        return self._numero_transacoes


class ContaCorrente(Conta):  # Extende a classe Conta. Herança simples

    def __init__(
        self,
        cliente: Cliente,
        numero: int,
        limite: float = 500.0,
        limite_transacoes: int = 10,
    ) -> None:
        super().__init__(cliente=cliente, numero=numero)

        self._limite = limite
        self._limite_transacoes = limite_transacoes


    def __str__(self) -> str:
        return (
            f"Agência: {self.agencia}, C/C: {self.numero}, Titular: {self.cliente.nome}"
        )


    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"


    @property
    def limite(self) -> float:
        return self._limite

    @property
    def limite_transacoes(self) -> int:
        return self._limite_transacoes


class ContaIterador:

    def __init__(self, contas) -> None:
        self.contas = contas
        self._index = 0


    def __iter__(self):
        return self


    def __next__(self):
        try:

            conta = self.contas[self._index]
            return f"""Agência: {conta.agencia}, Número: {conta.numero}, Titular: {conta.cliente.nome}, Saldo: R$ {conta.saldo:.2f}"""

        except IndexError:
            raise StopIteration

        finally:
            self._index += 1
