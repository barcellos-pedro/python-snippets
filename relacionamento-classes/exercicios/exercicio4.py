class Exame():
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_exame(self):
        print("> Dados do exame")
        print(f"Descrição: {self.descricao}")
        print(f"Resultado: {self.resultado}")
        print()
        print("## Dados do médico")
        print(f"Nome: {self.medico.nome}")
        print(f"CRM: {self.medico.crm}")
        print(f"Especialização: {self.medico.especializacao}")
        print()
        print("## Dados do paciente")
        print(f"Nome: {self.paciente.nome}")
        print(f"CPF: {self.paciente.cpf}")
        print(f"Idade: {self.paciente.idade}")

class Paciente():
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico():
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao



paciente = Paciente('Marcelo Silva', '033444555-22', 26)

medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')

exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						

