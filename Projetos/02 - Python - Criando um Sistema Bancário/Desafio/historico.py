from datetime import datetime

import pytz

from transacao import Transacao


class Historico:

    def __init__(self) -> None:
        self._transacoes = []
        self._mascara_datetime = "%Y/%m/%d %H:%M:%S"

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(pytz.timezone("UTC")),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):

        for transacao in self.transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self) -> int:

        data_atual = datetime.now(pytz.timezone("UTC"))
        dia_atual = data_atual.day

        numero_de_transacao = 0
        for transacao in self.transacoes:
            dia_transacao = transacao["data"].day

            if dia_transacao == dia_atual:
                numero_de_transacao += 1

        return numero_de_transacao

    @property
    def transacoes(self) -> list:
        return self._transacoes
