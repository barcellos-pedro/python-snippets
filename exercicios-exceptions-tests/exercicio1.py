"""
Identifique todas as exceções que podem ser geradas e
para cada uma, deve ser dado o tratamento adequado
que nesse exercício significa alertar o usuário quanto ao problema
"""


try:
    x = int(input('Primeiro valor: '))
    y = int(input('Segundo valor: '))

    z = x / y

    print('O resultado da divisão é:', z)

except ValueError:
    print(f"{ValueError.__name__} - Número informado não é inteiro")
except ZeroDivisionError:
    print(f"{ZeroDivisionError.__name__} - Divisão por zero")
except Exception:
    print("Erro inesperado")
