from test_main import somar

import unittest

class TestSomarFunction(unittest.TestCase):
    def test_somar_positivos(self):
        """Teste para somar dois números positivos."""
        self.assertEqual(somar(2, 3), 5)

    def test_somar_negativos(self):
        """Teste para somar dois números negativos."""
        self.assertEqual(somar(-2, -3), -5)

    def test_somar_zero(self):
        """Teste para somar números incluindo zero."""
        self.assertEqual(somar(0, 5), 5)
        self.assertEqual(somar(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(somar(1, 3), 4)

if __name__ == "__main__":
    unittest.main()
