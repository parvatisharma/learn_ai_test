import unittest
from factorial import factorial, factorial_recursive


class TestFactorial(unittest.TestCase):
    """Test cases for factorial functions."""
    
    def test_factorial_zero(self):
        """Test factorial of 0."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial_recursive(0), 1)
    
    def test_factorial_one(self):
        """Test factorial of 1."""
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial_recursive(1), 1)
    
    def test_factorial_positive(self):
        """Test factorial of positive numbers."""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial_recursive(10), 3628800)
    
    def test_factorial_negative(self):
        """Test factorial raises error for negative numbers."""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial_recursive(-1)
    
    def test_both_methods_equal(self):
        """Test that both methods produce the same results."""
        for n in range(15):
            self.assertEqual(factorial(n), factorial_recursive(n))


if __name__ == '__main__':
    unittest.main()
