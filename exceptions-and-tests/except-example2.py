from time import sleep


def main():
    try:
        a = int(input("Digite um número: "))
        b = int(input("Digite um número: "))
        c = a / b
        sleep(1)
        print(f"Valor da divisão: {c:.2f}")

    except ValueError:
        print(f"{ValueError.__name__} - Número informado não é inteiro")
    except ZeroDivisionError:
        print(f"{ZeroDivisionError.__name__} - Divisão por zero")
    except Exception:
        print("Erro inesperado")

    else:  # Só roda se não houver nenhum erro
        print("Operação feita com sucesso")
    finally:  # Sempre roda independente de erro
        print("Finalizando...")


main()
