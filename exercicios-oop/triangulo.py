class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return round(self.lado_a + self.lado_b + self.lado_c, 2)


lado_a = float(input("Digite a medida de um lado: "))
lado_b = float(input("Digite a medida de um lado: "))
lado_c = float(input("Digite a medida de um lado: "))

triangulo_1 = Triangulo(lado_a, lado_b, lado_c)

print(f"Perímetro = {triangulo_1.calcular_perimetro()}")
