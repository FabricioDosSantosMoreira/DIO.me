from transacao import Transacao
from datetime import datetime


class Historico():

    def __init__(self) -> None:
        self._transacoes = []


    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
            )
        
    
    def gerar_relatorio(self, tipo_transacao=None):

        # tipos = []
        # if not tipo_transacao:
        #     tipos = ["Deposito", "Saque"]

        # elif tipo_transacao == "Saque"

        for transacao in self.transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao
        

        
        
    @property
    def transacoes(self) -> list:
        return self._transacoes