import unittest
from operaciones.resta import restar



class TestRestar(unittest.TestCase):
  def test_restar(self):
    print('Testeando la función restar')
    self.assertEqual(restar(3, 2), 1)
    self.assertEqual(restar(-1, 1), -2)
    self.assertEqual(restar(-1, -1), 0)


if __name__ == '__main__':
  unittest.main()