from conversoes import converte_para_celsius, converte_para_fahrenheit

# Testes Celsius


def teste_celsius_1():
    try:
        test = converte_para_fahrenheit(0)
        esperado = 32.0
        assert test == esperado, "[FAILED] - Teste Celsius 1"
    except AssertionError as error:
        print(falha_msg(error))
        print(falha_valores(test, esperado))
    else:
        print("[OK] - Teste Celsius 1")
        print(sucesso_valores(test, esperado))


def teste_celsius_2():
    try:
        test = converte_para_fahrenheit(27)
        esperado = 80.6
        assert test == esperado, "[FAILED] - Teste Celsius 2"
    except AssertionError as error:
        print(falha_msg(error))
        print(falha_valores(test, esperado))
    else:
        print("[OK] - Teste Celsius 2")
        print(sucesso_valores(test, esperado))

# Testes Fahrenheit


def test_fahrenheit_1():
    try:
        test = converte_para_celsius(32)
        esperado = 0
        assert test == esperado, "[FAILED] - Teste Fahrenheit 1"
    except AssertionError as error:
        print(falha_msg(error))
        print(falha_valores(test, esperado))
    else:
        print("[OK] - Teste Fahrenheit 1")
        print(sucesso_valores(test, esperado))


def test_fahrenheit_2():
    try:
        test = converte_para_celsius(41)
        esperado = 5.0
        assert test == esperado, "[FAILED] - Teste Fahrenheit 2"
    except AssertionError as error:
        print(falha_msg(error))
        print(falha_valores(test, esperado))
    else:
        print("[OK] - Teste Fahrenheit 2")
        print(sucesso_valores(test, esperado))


def testes_celsius():
    """
    Roda todos os testes Celsius
    """
    print("Rodando testes Celsius...")
    teste_celsius_1()
    teste_celsius_2()


def testes_fahrenheit():
    """
    Roda todos os testes Fahrenheit
    """
    print("Rodando testes Fahrenheit...")
    test_fahrenheit_1()
    test_fahrenheit_2()


def sucesso_valores(valor, esperado):
    return f"--> {valor} igual a {esperado}"


def falha_valores(valor, esperado):
    return f"--> {valor} diferente de {esperado}"


def falha_msg(mensagem):
    return mensagem


def main():
    """
    Roda todos os testes
    """
    print("Rodando testes...")
    testes_celsius()
    testes_fahrenheit()


main()
