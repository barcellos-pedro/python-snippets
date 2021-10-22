class Carro:
    def __init__(self):
        self.qtd_combustivel = 0

    def adicionar_combustivel(self, litros):
        self.qtd_combustivel += litros

    def obter_combustivel(self):
        return self.qtd_combustivel

    def andar(self, distancia):
        self.qtd_combustivel = distancia / self.qtd_combustivel
        print(f"Percorrendo {distancia} KM...")


meu_carro = Carro()

meu_carro.adicionar_combustivel(20)  # Adiciona 20 litros
meu_carro.andar(80)  # Andar 80 KM

print('Litros de combustível no tanque: ', meu_carro.obter_combustivel())

# deve imprimir: "Litros de combustível no tanque: 4.0"

try:
    assert meu_carro.obter_combustivel() == 4.0, "[FAILED Test] - Combustivel"
except AssertionError as error:
    print(error)
else:
    print("[TEST OK]")
