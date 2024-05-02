class Bicicleta:

    def __init__(self, cor, modelo, ano, valor, marcha=10):
        self.modelo = modelo
        self.valor = valor
        self.ano = ano
        self.cor = cor

        self.marcha = marcha
        

    def buzinar(self):
        print("\nPlim plim...")

    def parar(self):
        print("\nParando bicicleta...")
        print("\nBicicleta parada!")


    def correr(self):
        print("\nVrummmmm...")


    def trocar_marcha(self, nmr_marcha):
        print("\nTrocando marcha...")

        def _trocar_marcha(self):
            if nmr_marcha > self.marcha:
                print("\nMarcha trocada!")

            else:
                print("\nNão foi possível trocar de marcha!")

        _trocar_marcha(self)


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
b2.trocar_marcha(10)