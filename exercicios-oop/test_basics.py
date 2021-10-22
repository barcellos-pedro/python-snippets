import unittest
from carro import Carro


class TestStringMethods(unittest.TestCase):

    meu_carro = Carro()

    meu_carro.adicionar_combustivel(20)
    meu_carro.andar(80)

    def test_combustivel(self):
        self.assertEqual(self.meu_carro.obter_combustivel(), 4.0)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
