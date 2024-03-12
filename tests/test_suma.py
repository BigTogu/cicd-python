import unittest
from operaciones.suma import sumar



class TestSumar(unittest.TestCase):
  def test_sumar(self):
    print('Testeando la función sumar')
    self.assertEqual(sumar(3, 2), 5)
    self.assertEqual(sumar(-1, 1), 0)
    self.assertEqual(sumar(-1, -1), -2)

if __name__ == '__main__':
  unittest.main()