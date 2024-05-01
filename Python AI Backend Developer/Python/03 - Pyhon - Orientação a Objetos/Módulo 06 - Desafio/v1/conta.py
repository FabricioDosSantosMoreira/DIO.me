from historico import Historico
from cliente import Cliente


class Conta():

    def __init__(self, cliente, numero: int) -> None:

        self._historico =  Historico()
        self._cliente = cliente

        self._numero = numero
        self._saldo: float = 0.0
        self._agencia: str = "0001"
        
        
    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(cliente, numero)

    
    def sacar(self, valor: float) -> bool:

        if valor > self.saldo: # O valor de saque excedeu o saldo?
            print("\nERRO - - -> A operação falhou. Você não possui saldo suficiente!")
            return False

        elif valor <= 0: # O valor de saque é inválido?
            print("\nERRO - - -> A operação falhou. O valor informado é inválido!")
            return False


        self._saldo -= valor
        print("\nSUCESSO - - -> Saque realizado com sucesso!")

        return True
    

    def depositar(self, valor: float) -> bool:

        if valor <= 0: # O valor de depósito é invalido?
            print("\nERRO - - -> A operação falhou. O valor informado é inválido!")
            return False


        self._saldo += valor
        print("\nSUCESSO - - -> Depósito realizado com sucesso!")

        return True
    

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'\n\t{chave}={str(valor)}' for chave, valor in self.__dict__.items()])}\n"


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
    def cliente(self) -> 'Cliente':
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico


class ContaCorrente(Conta): # Extende a classe Conta. Herança simples

    def __init__(self, cliente, numero: int, limite: float=500.0, limite_saques: int=3) -> None:
        super().__init__(cliente=cliente, numero=numero) 

        self._limite = limite
        self._limite_saques = limite_saques


    @property
    def limite(self) -> float:
        return self._limite
    
    @property
    def limite_saques(self) -> int:
        return self._limite_saques