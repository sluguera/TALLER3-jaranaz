import unittest
#import pytest
from boa_constrictor import BoaConstrictor
from ferret import Ferret

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        # Configuración para los objetos de prueba de Boa
        self.boa = BoaConstrictor("Boa1", 50.0, 5, "Brasil", 10.0)

    def test_hacer_sonido(self):
        boa = BoaConstrictor(name="Boa1", weight=50.0, age=5, country="Brasil", taxes=10.0)
        self.assertEqual(boa.do_sound(), "¡Tsss!")

    def test_calcular_flete(self):
        boa = BoaConstrictor(name="Boa1", weight=50.0, age=5, country="Brasil", taxes=10.0)
        expected_freight = boa.weight * boa.taxes
        self.assertEqual(boa.calculate_freight(), expected_freight)

    def test_eat_mouse_limit(self):
        boa = BoaConstrictor(name="Boa1", weight=50.0, age=5, country="Brasil", taxes=10.0)
        for _ in range(10):
            boa.eat_mouse()
        self.assertEqual(boa.eaten_mice, 10)
        # Intenta alimentar más allá del límite y verifica que lanza un ValueError
        with self.assertRaises(ValueError) as context:
            boa.eat_mouse()
            self.assertEqual(str(context.exception), "Demasiados Ratones!")


if __name__ == "__main__":
    unittest.main()