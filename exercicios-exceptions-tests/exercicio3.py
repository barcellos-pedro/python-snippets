"""
Preencha uma lista com 5 nomes de pessoas, informados pelo usuário.
Criar uma função que recebe como parâmetro de entrada a lista e um número
E retorna o nome que está na posição do número digitado
Essa função deve gerar e tratar uma exceção
do tipo IndexError caso o índice não exista na lista.
"""

lista = []

while len(lista) < 5:
    nome = input("Digite um nome: ")
    lista.append(nome)

print(f"Lista -> {lista}")


def get_nome(lista, numero):
    """
    Recebe uma lista e um número para servir como índice dessa lista

    Retorna o nome que está na posição do número informado

    Parâmetros:

    lista
    numero
    """
    try:
        return lista[numero]
    except IndexError:
        return f"[{IndexError.__name__}] - O índice informado não existe."


try:
    index = int(input("Digite um número para ser o índice: "))
    resultado = get_nome(lista, index)
except ValueError:
    print(f"[{ValueError.__name__}] - Valor digitado precisa ser numérico")
else:
    print(resultado)
