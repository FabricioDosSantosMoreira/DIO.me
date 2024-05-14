# TODO: Crie uma classe UsuarioTelefone.
class UsuarioTelefone():

    # TODO: Defina um método especial `__init__`, que é o construtor da classe.
    def __init__(self, nome: str, numero: str, plano: str) -> None:

        # O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
        self._nome: str = nome
        self._numero: str = numero
        self._plano: str = plano

    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
    @property 
    def nome(self) -> str:
        return self._nome
    
    @property 
    def numero(self) -> str:
        return self._numero
    
    @property 
    def plano(self) -> str:
        return self._plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self) -> str:
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  

# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)
