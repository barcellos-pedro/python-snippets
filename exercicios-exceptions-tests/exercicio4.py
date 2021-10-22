"""
Crie um dicionário para armazenar uma listagem de alunos

A) Utilize como chave o RA do aluno e como valor o nome do aluno

B) Os dados devem ser informados pelo usuário

C) O RA de cada aluno deve ser composto por
um número inteiro de exatamente 7 dígitos.

- Caso o RA informado não esteja no formato correto, deve ser gerada uma
exceção do tipo ValueError (utilize a instrução raise)

- Caso o RA informado já exista no dicionário, deve ser gerada uma exceção
do tipo TypeError (utilize a instrução raise)
"""


alunos = {}


for i in range(3):
    try:
        ra = int(input('RA: '))
        if len(str(ra)) < 7 or len(str(ra)) > 7:
            raise ValueError
        if ra in alunos:
            raise TypeError
        nome = input('Nome: ')
        alunos[ra] = nome
    except ValueError:
        print("[RA ERROR] - Digite um RA no padrão e com 7 Digitos.")
    except TypeError:
        print(f"[RA ERROR ] - O RA [{ra}] já existe.")
    except Exception:
        print("Erro inesperado.")

for key in alunos:
    print(f"RA: {key} -> Nome: {alunos[key]}")
