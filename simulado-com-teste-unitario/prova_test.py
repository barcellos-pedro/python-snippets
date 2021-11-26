
import unittest

from prova import Episodio, Serie

game_of_thrones = Serie("Game of Thrones")
stranger_things = Serie("Stranger Things")

got_ep1 = Episodio(1, 1, "Winter Is Coming", 63)
got_ep2 = Episodio(2, 1, "The Kingsroad", 56)
got_ep3 = Episodio(3, 1, "Lord Snow", 103)

st_ep1 = Episodio(1, 1, "Chapter One: The Vanishing of Will Byers", 47)
st_ep2 = Episodio(2, 1, "Chapter Two: The Weirdo on Maple Street", 55)
st_ep3 = Episodio(3, 1, "Chapter Three: Holly, Jolly", 51)

game_of_thrones.incluir_episodio(got_ep1)
game_of_thrones.incluir_episodio(got_ep2)
game_of_thrones.incluir_episodio(got_ep3)

stranger_things.incluir_episodio(st_ep1)
stranger_things.incluir_episodio(st_ep2)
stranger_things.incluir_episodio(st_ep3)


class TestStringMethods(unittest.TestCase):

    def test_epi_duracao(self):
        self.assertEqual(got_ep1.duracao, 63)

    def test_buscar_episodios(self):
        """
        Busca todos os episódios da 8ª temporada de Game of Thrones
        """
        temporada = 8
        lista = game_of_thrones.buscar_episodios(temporada)

        for ep in lista:
            self.assertEqual(ep.temporada, temporada)

    def test_incluir_episodio(self):
        """
        Inclui um episodio em uma lista
        """
        lista = []
        epi = Episodio(99, 99, "Broklyn 99", 99)

        self.assertEqual(lista, [])
        lista.append(epi)
        self.assertGreater(len(lista), 0)


if __name__ == '__main__':
    unittest.main()
