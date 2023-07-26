"""
Run using the following command: `python -m unittest test_calc.py`

Alternatively, if you want to run tests by running `python test_calc.py`, 
at the end of the code you can add the following:
```py
if __name__ == '__main__':
    unittest.main()

"""
# standard library
import unittest

import calc

# unittest.TestCase has lots of functions for doing tests
class TestCalc(unittest.TestCase):

    # functions within this class have to start with a prefix `test_`; 
    # if they do not start like that, then these functions will be skipped
    # during the test
    def test_add(self):
        """
        all of these three detailed test cases testing edge cases 
        still count as 1 test in the terminal output, 
        as they are defined within the same function
        """
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        ### check if raises error
        ### METHOD 1: 
        self.assertRaises(ValueError, calc.divide, 10, 0)
        ### METHOD 2: context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
