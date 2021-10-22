class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @classmethod
    def from_string(cls, data):
        """
        Alternative constructor to create new object from kebab-case string
        >>> "Name-5500"
        >>> "Funcionario('Name', 5500)"
        """
        nome, salario = data.split("-")
        return cls(nome, float(salario))

    @staticmethod
    def boas_vindas():
        return "Olá"

    def aumentar_salario(self, percentual):
        self.salario = self.salario * percentual


nome = input("Digite seu nome: ")
salario = float(input("DIgite seu salário: "))

funcionario_1 = Funcionario(nome, salario)
funcionario_2 = Funcionario.from_string("Pedro-3000")

percentual_aumento = float(input("Digite o % para aumento: "))

funcionario_1.aumentar_salario(percentual_aumento)

print()

print(funcionario_1.boas_vindas())
print(f"Funcionário {funcionario_1.nome}")
print(f"Salário: {funcionario_1.salario}")

print()

print(Funcionario.boas_vindas())
print(f"Funcionário {funcionario_2.nome}")
print(f"Salário: {funcionario_2.salario}")
