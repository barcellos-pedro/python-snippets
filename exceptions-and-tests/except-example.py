texto = input("Digite alguma coisa: ")


def main(texto):
    try:
        if len(texto) == 0 or texto.strip() == '':
            raise ValueError
    except ValueError:
        print(f"{ValueError.__name__} - Texto sem caractere [{texto}]")
    else:
        print(f"Valor digitado -> {texto}")
    finally:
        print("Finalizando...")


main(texto)
