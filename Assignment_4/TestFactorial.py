import unittest
import factorial as f # Correct import



class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(f.factorial(5), 120)
       
    
    def test_factorial_negative(self):
        with self.assertRaises(RecursionError) as context:  # Since negative numbers cause infinite recursion
            f.factorial(-2)
        self.assertEqual(str(context.exception), "No Negative")

    def test_factorial_non_integer(self):
        self.assertEqual(f.factorial("abc"), 'Only positive integers are allowed!')
        self.assertEqual(f.factorial(3.5), 'Only positive integers are allowed!')
        self.assertEqual(f.factorial(None), 'Only positive integers are allowed!')
       
        
if __name__ == '__main__':
    unittest.main()
