class Episodio():
    def __init__(self, numero, temporada, nome, duracao):
        self.numero = numero
        self.temporada = temporada
        self.nome = nome
        self.duracao = duracao


class Serie:
    def __init__(self, nome):
        self.nome = nome
        self.episodios = []

    def incluir_episodio(self, episodio):
        self.episodios.append(episodio)

    def buscar_episodios(self, temporada):
        resultado = [ep for ep in self.episodios if ep.temporada == temporada]
        return resultado
