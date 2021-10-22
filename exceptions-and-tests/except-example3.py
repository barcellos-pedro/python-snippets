# Solicitar um numero inter e positivo
# Gerar exceção se o número não for inteiro e positivo

try:
    n = int(input("Informe um numero inteiro e positivo: "))
    if n < 0:
        raise TypeError
except TypeError:
    print("O número não é positivo")
except ValueError:
    print("O número não é inteiro")
