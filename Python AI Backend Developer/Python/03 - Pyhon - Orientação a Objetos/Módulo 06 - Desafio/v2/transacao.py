from abc import ABC, abstractmethod


class Transacao(ABC): # Classe abstrata que herda as funcionalidades fornecidas pelo módulo ABC (Abstract Base Classes) do Python
    
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao): # Extende a classe Transacao. Herança simples

    def __init__(self, valor: float) -> None:
        self._valor = valor


    def registrar(self, conta):

        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


    @property
    def valor(self) -> float:
        return self._valor
    

class Saque(Transacao): # Extende a classe Transacao. Herança simples

    def __init__(self, valor: float) -> None:
        self._valor = valor


    def registrar(self, conta):

        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


    @property
    def valor(self) -> float:
        return self._valor