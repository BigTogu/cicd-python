import unittest
from division import dividir



class TestDividir(unittest.TestCase):
  def test_dividir(self):
    self.assertEqual(dividir(6, 3), 2)
    self.assertEqual(dividir(0, 12), 0)
    self.assertEqual(dividir(-1, -1), 1)
    self.assertRaises(ValueError, dividir, 1, 0)


if __name__ == '__main__':
  unittest.main()