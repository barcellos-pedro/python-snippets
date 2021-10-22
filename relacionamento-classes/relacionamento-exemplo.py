class Endereco():
    def __init__(self, rua, numero, cep):
        self.rua = rua
        self.numero = numero
        self.cep = cep

    def exibir_dados(self):
        print(f"Rua: {self.rua}")
        print(f"Numero: {self.numero}")
        print(f"CEP: {self.cep}")


class Pessoa():
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Sexo: {self.sexo}")
        print(f"Endereco:")
        self.endereco.exibir_dados()


endereco_1 = Endereco("Av paulista", 100, 23498223)
pessoa_1 = Pessoa("Pedro", 24, "Masculino", endereco_1)

pessoa_1.exibir_dados()

