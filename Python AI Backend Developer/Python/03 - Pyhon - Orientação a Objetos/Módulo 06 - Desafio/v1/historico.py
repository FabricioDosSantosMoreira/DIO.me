from transacao import Transacao

from datetime import date, datetime


class Historico():

    def __init__(self) -> None:
        self._transacoes = []


    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
            )
        
    @property
    def transacoes(self) -> list:
        return self._transacoes