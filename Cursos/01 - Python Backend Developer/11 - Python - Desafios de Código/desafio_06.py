# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone():
    def __init__(self, nome: str, numero: str, plano: 'Plano') -> None:
        self.nome: str = nome
        self.numero: str = numero
        self.plano: Plano = plano

    # TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario: str, duracao: int) -> str:

        # TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
        custo_chamada = self.plano.custo_chamada(duracao)
        
        # TODO: Verifique se o saldo do plano é suficiente para a chamada.
        saldo = self.plano.verificar_saldo()
        if custo_chamada <= saldo:

            # TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
            self.plano.deduzir_saldo(custo_chamada)
            saldo = self.plano.verificar_saldo()

            # TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo:.2f}"

        return f"Saldo insuficiente para fazer a chamada."


# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial: float) -> None:
        self.saldo: float = saldo_inicial

    # TODO: Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self) -> float:
        return self.saldo

    # TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self, duracao) -> float:
        CUSTO = 0.10
        return CUSTO * duracao

    # TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:
    def deduzir_saldo(self, valor) -> None:
        self.saldo -= valor


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):

    def __init__(self, nome: str, numero: str, saldo_inicial: float) -> None:
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
