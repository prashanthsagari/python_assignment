import unittest
import NegativeNumberError as ne
import SquareRoot as sq


class TestFactorial(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(sq.square_root(25), 5.0)
    
    def test_negative_number(self):
        with self.assertRaises(ne.NegativeNumberError) as context:
            sq.square_root(-4)
        self.assertEqual(str(context.exception), "Only positive numbers are allowed !!!")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sq.square_root("abc")
        with self.assertRaises(TypeError):
            sq.square_root([4])
        with self.assertRaises(TypeError):
            sq.square_root(None)

if __name__ == '__main__':
    unittest.main()
