class Emprego():
    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus


class Pessoa():
    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []

    def calcular_salario(self):
        num_dependentes = len(self.dependentes)
        bonus_total = num_dependentes * self.emprego.bonus / 100 
        percentual = 1.0 + bonus_total
        return self.emprego.salario * percentual


emprego = Emprego("Programador", "TI", 1000, 5)

pessoa1 = Pessoa("Paulo", "11-99999999", "paulo@email.com", emprego)

dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

pessoa1.dependentes.append(dep1)
pessoa1.dependentes.append(dep2)

print(f"Salario: {pessoa1.calcular_salario()}")

